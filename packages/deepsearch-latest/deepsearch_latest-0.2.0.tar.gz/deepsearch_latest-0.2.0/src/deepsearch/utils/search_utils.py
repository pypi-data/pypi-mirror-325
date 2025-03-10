import asyncio
import aiohttp
import logging

from deepsearch.utils.upload_to_cloudflare import CloudflareUploader
from deepsearch.utils.pinecone_utils import PineconeManager
from deepsearch.utils.openrouter_utils import split_and_extract_information
from deepsearch.utils.async_utils import log_cancellation

logger = logging.getLogger("deepsearch-mcp")


@log_cancellation
async def perform_search_analysis(
    query: str,
    pinecone_client: PineconeManager,
    cloudflare_uploader: CloudflareUploader
) -> list[dict]:
    """
    Perform search analysis using Pinecone and Cloudflare
    """
    logger.info("Starting document retrieval and analysis...")

    # Step 1: Get search results and fetch documents
    search_results = pinecone_client.search_documents(query, min_score=0.2)
    logger.info(f"Retrieved {len(search_results)} documents")

    # Step 2: Fetch documents
    documents = await async_fetch_all_documents(search_results, cloudflare_uploader)

    # Step 3: Process with OpenRouter
    processed_results = await async_process_documents_with_openrouter(query, documents)

    # Combine results
    all_results = [
        {
            'source': doc_path,
            'score': next(r['normalized_score'] for r in search_results if r['cloudflare_path'] == doc_path),
            'extracted_info': info
        }
        for doc_path, info in processed_results.items()
    ]

    return sorted(all_results, key=lambda x: x['score'], reverse=True)


@log_cancellation
async def async_fetch_all_documents(search_results, cloudflare_uploader) -> dict:
    """Fetch all documents concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [
            cloudflare_uploader._fetch_document_text(doc['cloudflare_path'])
            for doc in search_results
        ]
        texts = await asyncio.gather(*tasks)
        return {
            result['cloudflare_path']: text
            for result, text in zip(search_results, texts)
            if text
        }


@log_cancellation
async def async_process_documents_with_openrouter(query: str, documents: dict) -> dict:
    """Process all documents with OpenRouter concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [
            split_and_extract_information(query, text, session=session)
            for text in documents.values()
        ]
        results = await asyncio.gather(*tasks)
        return {
            doc_path: result
            for (doc_path, _), result in zip(documents.items(), results)
            if result
        }
