import os
from open_webui.apps.retrieval.main import app as retrieval_app
from open_webui.apps.retrieval.utils import get_sources_from_files
from open_webui.utils.task import rag_template
from open_webui.utils.misc import (
    add_or_update_system_message,
    get_last_user_message,
    prepend_to_first_user_message_content,
)
from CafeRAG import config
from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

folder_path = '/app/backend/data/CafeRAG/knowledge_files/'
file_path = 'Tortoise and the Hare.docx'

def fusion(payload):
    config_data = config.read_file_config()
    if config.read_config('Fusion_state', config_data):
        sources = loaddata(file_path=folder_path + file_path)
        # If context is not empty, insert it into the messages
        if len(sources) > 0:
            context_string = ""
            for source_idx, source in enumerate(sources):
                # Accessing the page_content directly
                doc_context = source.page_content
                metadata = source.metadata
                source_id = metadata.get("source", "")
 
                if source_id:
                    context_string += f"<source><source_id>{source_id}</source_id><source_context>{doc_context}</source_context></source>\n"
                else:
                    context_string += f"<source><source_context>{doc_context}</source_context></source>\n"
 
        context_string = context_string.strip()
        prompt = get_last_user_message(payload["messages"])
        print("Injected RAG")
        return inject(payload, context_string, prompt)
    else:
        return payload

def inject(body, context_string, prompt):
    body["messages"] = add_or_update_system_message(
        rag_template(
            retrieval_app.state.config.RAG_TEMPLATE, context_string, prompt
        ),
        body["messages"],
    )

    return body

def loaddata(path):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=30)
    
    if os.path.isfile(path):
        loader = Docx2txtLoader(path)
        doc = loader.load()
        docs = text_splitter.split_documents(doc)
        return docs
    
    elif os.path.isdir(path):
        arr_docs = []
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                loader = Docx2txtLoader(file_path)
                doc = loader.load()
                docs = text_splitter.split_documents(doc)
                arr_docs.extend(docs)
        return arr_docs
    else:
        raise ValueError("The provided path is neither a file nor a directory")