from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
  "我的邻居姓{last_name}，他的孩子性别是{gender}，你帮忙起一个名字，简单回答"
)

model = Tongyi(model = "qwen-max")

chain = prompt_template | model
res = chain.invoke(input = {"last_name": "容", "gender": "女"})
print(res)

# # 调用format方法注入 
# prompt_text = prompt_template.format(last_name="容", gender="女")

# model = Tongyi(model = "qwen-max")
# res = model.stream(prompt_text)
# for r in res:
#   print(r, end="",flush=True)





