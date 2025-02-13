document_summary_prompt = """
You are a librarian that stores documents in a database for a company called Digestiva. The company produces an enzyme produce and is engaged in both research as well as production. 
Given a document titled '{document_name}', you need to think deeply about the document and then create a description of the document that can be used to retrieve the document at a later time.
Do not return anything expect for the description of the document. The description should include all key information about the document such that if someone was searching for a small piece of information that is included within the document, they would be able to know that this document contains that information. Pay special attention to including any names of people, companies, organizations, and any dates mentioned in the document.

Here is the document:
{document}

Here is a description of the document focused on capturing the key information that would allow someone to retrieve this document if they were searching for specific details contained within it, including all names of people, companies, organizations and dates:
"""

pdf_transcription_prompt = "Transcribe all text from this pdf page exactly as written, with no introduction or commentary. For any unclear or uncertain text, use {probably - description} format in place of the text."

information_extraction_prompt = """You are an information extraction expert focused on maximum information preservation. Your task is to thoroughly analyze the provided document and extract ALL information that could be even remotely relevant to the given query. Be extremely conservative in what you exclude - if there's any doubt about whether information might be relevant, include it.

Include:
- Directly relevant information
- Contextual details
- Background information
- Related facts or data
- Supporting details
- Any information that provides additional context or could be useful for understanding the topic
- Format and display any tables using markdown table syntax, preserving all data exactly as shown

DO NOT:
- Summarize or condense the information
- Draw conclusions
- Answer the query
- Exclude information just because it seems only tangentially related
- Describe tables in text - always display them in proper table format

Query: {query}

Document:
{document}

Here is ALL the potentially relevant information extracted from the document, preserving as much detail as possible and displaying any tables in proper format:
"""
