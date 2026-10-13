# from app.core.config import get_settings
# settings=get_settings()
# print(f"App NAme: {settings.app_name}\n")
# print(f"Pinecone api : {settings.pinecone_api_key}")


from app.services.ingestion import load_file,chunk_documents
from pathlib import Path

docs=load_file(Path("data/sample_kb/company_it_handbook.md"))
chunk=chunk_documents(docs)
# print(docs)
# print(len(chunk))



from app.rag.vectorstore import add_documents
add_documents(chunk)
