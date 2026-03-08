from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型，默认使用 text-embedding-v1 模型
model = DashScopeEmbeddings()

# 调用embed_query和embed_documents方法
# 调用embed_query方法，返回单个向量（单个）
# 调用embed_documents方法，返回多个向量（批量）
print(model.embed_query("hello world"))
print(model.embed_documents(["hello world", "goodbye world"]))