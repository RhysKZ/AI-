from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./资料/数据资料/Python基础语法.txt", encoding="utf-8")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,                  # 每个文档的最大字符数
    chunk_overlap=10,                # 每个文档的最大重叠字符数
    separators=["\n\n", "\n", " ", "，", "。", "！", "？", "；", "：", "!", "?"],  # 分隔符列表
    length_function=len,            # 计算字符数的函数
)

print(len(splitter.split_documents(docs)))
for doc in splitter.split_documents(docs):
    print("="*20)
    print(doc)
    print("="*20)