from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path = "./资料/数据资料/pdf2.pdf",
    mode = "single",
    password = "itheima"
)

for doc in loader.lazy_load():
    print("="*100)
    print(doc)
    print("="*100)