from openai import OpenAI
# 1、获取client对象，OpenAI类对象
client = OpenAI(
  base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2、调用AI模型
response = client.chat.completions.create(
  model = "qwen3-max",
  messages = [
    {"role" : "system" , "content" : "你是一个python编程专家"},
    {"role" : "assistant" , "content" : "我是一个python编程专家，你需要我为你解决什么问题"},
    {"role" : "system" , "content" : "写一个代码输出数字1-10"}
  ],
  stream = True  # 开启流式输出
)

# 3、处理结果
for chunk in response:
    if chunk.choices[0].delta.content:
        print(
            chunk.choices[0].delta.content, 
            end = " ",   # 每日一段之间使用空格分隔
            flush = True # 刷新输出缓冲区，确保实时显示
        )