from deepsearch.utils.search_utils import perform_search_analysis
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("deepsearch")


@server.tool()
async def perform_analysis(
    query: str,
    output_dir: str = "test_output",
    outlier_method: str = 'zscore',
    outlier_threshold: float = 1
) -> str:
    """Perform search analysis on the given query.

    Args:
        query: The search query to analyze
        output_dir: Directory to store output files
        outlier_method: Method for outlier detection ('zscore' or other supported methods)
        outlier_threshold: Threshold value for outlier detection

    Returns:
        Formatted string containing all search results with sources, scores, and extracted information
    """
    results = await perform_search_analysis(
        query=query,
        output_dir=output_dir,
        outlier_method=outlier_method,
        outlier_threshold=outlier_threshold
    )

    # Format results into a single string
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

    return "\n".join(formatted_output)
