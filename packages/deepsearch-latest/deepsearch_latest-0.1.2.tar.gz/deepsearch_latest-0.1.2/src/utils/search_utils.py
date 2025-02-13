import pandas as pd
import numpy as np
import asyncio
import aiohttp

from utils.upload_to_cloudflare import CloudflareUploader
from utils.pinecone_utils import PineconeManager
from utils.retrieval_utils import retrieve_and_analyze_documents
from utils.openrouter_utils import extract_information


def find_outliers(scores: pd.Series, method: str = 'zscore', threshold: float = 2.0) -> pd.Series:
    if method == 'zscore':
        z_scores = np.abs((scores - scores.mean()) / scores.std())
        return z_scores > threshold
    elif method == 'iqr':
        Q1 = scores.quantile(0.25)
        Q3 = scores.quantile(0.75)
        IQR = Q3 - Q1
        return (scores > Q3 + threshold * IQR) | (scores < Q1 - threshold * IQR)
    else:
        raise ValueError("Method must be either 'zscore' or 'iqr'")


async def perform_search_analysis(
    query: str,
    output_dir: str = "test_output",
    outlier_method: str = 'zscore',
    outlier_threshold: float = 1,
    model: str = "openai/o3-mini"
):
    print("Starting document retrieval and analysis...")

    # Get initial results and scores
    results, raw_scores, normalized_scores, full_texts = await retrieve_and_analyze_documents(query)
    print(f"Retrieved {len(results)} documents")

    # Initialize managers
    uploader = CloudflareUploader()
    pinecone = PineconeManager()

    # Prepare tasks for parallel extraction
    extraction_tasks = []
    all_results = []

    # Create a single session for all API calls
    async with aiohttp.ClientSession() as session:
        for i, doc in enumerate(results, 1):
            print(
                f"\nProcessing document {i}/{len(results)}: {doc['cloudflare_path']}")

            # Fetch full text from Cloudflare
            full_text = uploader._fetch_document_text(doc['cloudflare_path'])
            if not full_text:
                print(f"Could not fetch text for document {i}")
                continue

            # Score full document with Pinecone's rerank
            reranked = pinecone.pc.inference.rerank(
                model="cohere-rerank-3.5",
                query=query,
                documents=[full_text],
                top_n=1,
                return_documents=True
            )
            doc_score = reranked.data[0].score

            # Create a task to call extract_information in parallel
            extraction_tasks.append(
                extract_information(query, full_text, session=session)
            )

            # Save partial info to all_results
            all_results.append({
                'score': doc_score,
                'text': full_text,
                'source_path': doc['cloudflare_path'],
                'extracted_info': None  # Will be filled after gather completes
            })

        # Execute all extraction tasks in parallel
        extracted_info_list = await asyncio.gather(*extraction_tasks)

    # Assign each extracted_info to the corresponding record
    for i in range(len(all_results)):
        all_results[i]['extracted_info'] = extracted_info_list[i]

    # Sort by score and return extracted information
    sorted_results = sorted(
        all_results, key=lambda x: x['score'], reverse=True)
    return [{'source': r['source_path'],
             'score': r['score'],
             'extracted_info': r['extracted_info']}
            for r in sorted_results]
