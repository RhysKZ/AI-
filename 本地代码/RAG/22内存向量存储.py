from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vec_store = InMemoryVectorStore(
  embedding = DashScopeEmbeddings(),
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
vec_store.delete(
    ids = ["id1","id2"]  # 删除的文档的id
)

# 检索
print(vec_store.similarity_search("明天晚上吃啥子呀"))
