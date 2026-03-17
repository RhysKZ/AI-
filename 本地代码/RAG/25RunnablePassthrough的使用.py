from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document


# 模型
model = ChatTongyi(model="qwen-plus")
# 提示词
prompt = ChatPromptTemplate.from_messages([
    ("system", "以我提供的已知参考资料为主，简洁专业的回答用户的问题，参考资料：{context}"),
    ("human", "用户提问：{input}")
])
# 内存向量存储
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

# 准备数据
vector_store.add_texts(["减脂就是要少吃多练", "在减肥期间吃东西很重要,清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动哦"])

input_text = "我该如何减肥"

# langchain中向量存储对象，有一个as_retriever方法，可以返回一个Runnable接口的子类实例
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

def format_func(docs: list[Document]):
  if not docs:
    return "无相关参考资料"
  formatted_str = "["
  for doc in docs:
    formatted_str += doc.page_content
    formatted_str += "，"
  formatted_str += "]"
  return formatted_str

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*100)
    return prompt

chain = {"input": RunnablePassthrough(), "context": retriever | format_func} | prompt | print_prompt | model | StrOutputParser()

res = chain.invoke(input_text)

print(res)