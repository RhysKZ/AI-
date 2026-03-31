md5_path = "./md5.text"
file_type = ["txt","pdf","docx","doc"]
collection_name = "rag"
persist_directory = "./chromadb"
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
max_split_char_number = 1000 # 文本分割的阈值
