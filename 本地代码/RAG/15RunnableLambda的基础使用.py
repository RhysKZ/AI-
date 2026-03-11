from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model="qwen3-max")
str_parser = StrOutputParser()
my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

first_prompt = PromptTemplate.from_template(
  "我邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。"
  "要求是key是name，value就是起的名字，请严格遵守格式要求。"
)

second_prompt = PromptTemplate.from_template(
  "你起的姓名：{name}，请解析这个名字的含义，并在起一个新的姓名"
)

chain = first_prompt | model | my_func | second_prompt | model | str_parser
# chain = first_prompt | model | (lambda ai_msg: {"name": ai_msg.content}) | second_prompt | model | str_parser


# res = chain.invoke({"lastname": "刘付", "gender": "女"})
# print(res.content)

chunk : str = chain.stream({"lastname": "刘付", "gender": "女"})
for res  in chunk:
  print(res, end="", flush=True)
