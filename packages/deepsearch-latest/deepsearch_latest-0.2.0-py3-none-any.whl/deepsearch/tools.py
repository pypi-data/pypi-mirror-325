import logging
from typing import Sequence, Union
from enum import Enum
import mcp.types as types
from mcp.server import Server
from deepsearch.utils.search_utils import async_fetch_all_documents, async_process_documents_with_openrouter
from deepsearch.utils.pinecone_utils import PineconeManager
from deepsearch.utils.upload_to_cloudflare import CloudflareUploader
from deepsearch.utils.async_utils import log_cancellation

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("deepsearch-mcp")


class ToolName(str, Enum):
    PERFORM_ANALYSIS = "perform-analysis"


ServerTools = [
    types.Tool(
        name=ToolName.PERFORM_ANALYSIS,
        description="Passes the user query and uses it to search across the database documents.",
        inputSchema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural language query to search across database documents"
                }
            },
            "required": ["query"],
        },
    ),
]


@log_cancellation
async def perform_search_analysis(
    query: str,
    pinecone_client: PineconeManager,
    cloudflare_uploader: CloudflareUploader,
    request_id: str,
    inflight_requests: dict
) -> Sequence[Union[types.TextContent, types.ImageContent, types.EmbeddedResource]]:
    """
    Perform search analysis using Pinecone and Cloudflare
    """
    try:
        inflight_requests[request_id] = "running"

        if not query:
            logger.error("Empty query provided")
            raise ValueError("Query parameter is required")

        logger.info("Starting document retrieval and analysis...")

        # Check for cancellation before expensive operations
        if inflight_requests.get(request_id) == "cancelled":
            logger.info(
                f"Request {request_id} was cancelled before processing")
            return []

        # Step 1: Get search results and fetch documents
        logger.info(f"Searching Pinecone with query: {query}")
        search_results = pinecone_client.search_documents(query, min_score=0.2)
        logger.info(f"Retrieved {len(search_results)} documents from Pinecone")

        if inflight_requests.get(request_id) == "cancelled":
            logger.info(
                f"Request {request_id} was cancelled after Pinecone search")
            return []

        # Step 2: Fetch documents
        logger.info("Fetching document contents from Cloudflare...")
        documents = await async_fetch_all_documents(search_results, cloudflare_uploader)
        logger.info(
            f"Successfully fetched {len(documents)} documents from Cloudflare")

        if inflight_requests.get(request_id) == "cancelled":
            logger.info(
                f"Request {request_id} was cancelled after document fetch")
            return []

        # Step 3: Process with OpenRouter
        logger.info("Processing documents with OpenRouter...")
        processed_results = await async_process_documents_with_openrouter(query, documents)
        logger.info(
            f"Successfully processed {len(processed_results)} documents with OpenRouter")

        if inflight_requests.get(request_id) == "cancelled":
            logger.info(
                f"Request {request_id} was cancelled after OpenRouter processing")
            return []

        # Combine results
        logger.info("Combining and sorting results...")
        all_results = [
            {
                'source': doc_path,
                'score': next(r['normalized_score'] for r in search_results if r['cloudflare_path'] == doc_path),
                'extracted_info': info
            }
            for doc_path, info in processed_results.items()
        ]

        results = sorted(all_results, key=lambda x: x['score'], reverse=True)

        if not results:
            logger.warning("No results found for the query")
            return [types.TextContent(type="text", text="No results found for the given query.")]

        # Format output
        logger.info("Formatting final output...")
        formatted_output = []
        for result in results:
            section = [
                f"\nSource: {result['source']}",
                f"Score: {result['score']:.3f}",
                "Extracted Information:",
                f"{result['extracted_info']}",
                "=" * 80
            ]
            formatted_output.append("\n".join(section))

        inflight_requests[request_id] = "done"
        logger.info(
            f"Search analysis completed successfully for request {request_id}")
        return [types.TextContent(type="text", text="\n".join(formatted_output))]

    except Exception as e:
        logger.error(f"Error in perform_search_analysis: {str(e)}")
        inflight_requests[request_id] = "error"
        raise


def register_tools(server: Server, pinecone_client: PineconeManager, cloudflare_uploader: CloudflareUploader, inflight_requests: dict):
    @server.list_tools()
    @log_cancellation
    async def handle_list_tools() -> list[types.Tool]:
        return ServerTools

    @server.call_tool()
    @log_cancellation
    async def handle_call_tool(
        name: str, arguments: dict | None
    ) -> Sequence[Union[types.TextContent, types.ImageContent, types.EmbeddedResource]]:
        try:
            # You'll need to ensure this is passed
            request_id = arguments.get("__request_id__")
            logger.info(f"Calling tool: {name} for request {request_id}")

            if name == ToolName.PERFORM_ANALYSIS:
                return await perform_search_analysis(
                    query=arguments.get("query"),
                    pinecone_client=pinecone_client,
                    cloudflare_uploader=cloudflare_uploader,
                    request_id=request_id,
                    inflight_requests=inflight_requests
                )
            else:
                logger.error(f"Unknown tool: {name}")
                raise ValueError(f"Unknown tool: {name}")
        except Exception as e:
            logger.error(f"Error calling tool {name}: {str(e)}")
            raise


__all__ = [
    "register_tools",
]
