# langchain_community
from langchain_community.llms.tongyi import Tongyi

# 初始化模型
model = Tongyi(model = "qwen-max")

# 调用invoke向模型发送请求
res = model.invoke("讲一个冷笑话")
print(res)