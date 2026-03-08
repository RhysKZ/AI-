from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model = "qwen-max")

res = model.stream("讲一个冷笑话")

for r in res:
  print(r, end="",flush=True)