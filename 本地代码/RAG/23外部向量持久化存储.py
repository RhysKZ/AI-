from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

# 向量数据库 chroma chromadb

vec_store = Chroma(
    collection_name = "test",                     #集合名
    embedding_function = DashScopeEmbeddings(),   # 嵌入模型
    persist_directory = "./本地代码/chat_history/chromadb",  # 向量数据库的目录

)

loader = CSVLoader(
    file_path = "./资料/数据资料/info.csv",
    encoding = "utf-8",
    source_column = "source", # 指定源文档的列名
)

documents = loader.load()

# 向量存储 
# 新增
vec_store.add_documents(
    documents = documents,                                    # 新增的文档
    ids = ["id" + str(i) for i in range(1, len(documents) + 1)]  # 新增的文档的id
)
# 删除
vec_store.delete(["id1","id2"])  # 删除的文档的id

# 检索
result = vec_store.similarity_search(
    "Python是世界上最好的编程语言",
    3,        # 检索的结果要几个
    filter={"source": "黑马程序员"}
)

print(result)
