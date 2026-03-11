from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

import uuid

model = ChatTongyi(model="qwen3-max")

# prompts = PromptTemplate.from_template(
#   "你是一个厨师，你需要根据会话历史回应用户问题。对话历史：{chat_history}，用户提问：{input}，请回答"
# )

prompts = ChatPromptTemplate.from_messages([
  ("system", "你是一个厨师，你需要根据会话历史回应用户问题。"),
  MessagesPlaceholder("chat_history"),
  ("human", "{input}"),
])

src_parser = StrOutputParser()

base_chain = prompts | model | src_parser

# key就是session_id,value就是会话历史数据
store = {}

# 实现通过会话ID从会话历史中获取历史记录的函数
def get_history(session_id):
  if session_id not in store:
    store[session_id] = InMemoryChatMessageHistory()
  return store[session_id]


# 创建一个新的链，对原有链增强功能：自动附加历史会话
conversation_chain = RunnableWithMessageHistory(
  base_chain,                            # 被增强的原有的chain
  get_history,                           # 通过会话ID从会话历史中获取历史记录的函数
  input_messages_key="input",            # 输入中包含用户问题的占位符
  history_messages_key="chat_history",   # 输入中包含历史会话的占位符
)

if __name__ == "__main__":
  # 固定格式，添加Langchain的配置，为当前程序配置所属的session_id
  session_config = {
    "configurable": {
      "session_id": uuid.uuid4().hex,
    }
  }

res = conversation_chain.invoke({"input": "小明买了豆腐，可以做什么菜"},session_config)
print("第一执行")
print(res)
res = conversation_chain.invoke({"input": "小红又买了肉沫，可以做什么菜"},session_config)
print("第二执行")
print(res)
res = conversation_chain.invoke({"input": "你再买两样东西，你可以做成出什么菜？"},session_config)
print("第三执行")
print(res)