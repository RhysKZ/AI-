from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi


chat_prompt_template = ChatPromptTemplate.from_messages(
  [
    ("system", "你是一个边塞诗人"),
    MessagesPlaceholder("history"),
    ("human", "请以与妻信告安为题再来一首边塞诗"),
  ]
)

history_data = [
    ("human", "请写一首诗"),
    ("ai", "床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "好诗再来一个"),
    ("ai", "锄禾日当午，汗滴禾下锄，谁知盘中餐，粒粒皆辛苦"),
]

model = ChatTongyi(model = "qwen3-max")

# 组成链，要求每一个组件都是Runable的接口子类
chain = chat_prompt_template | model

# 通过链调用invoke或stream方法
# res = chain.invoke(input={"history": history_data})
# print(res.content)

for chunk in chain.stream(input={"history": history_data}):
  print(chunk.content, end="", flush=True)




