from openai import OpenAI
# 1、获取client对象，OpenAI类对象
client = OpenAI(
  base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2、调用AI模型
response = client.chat.completions.create(
  model = "qwen3-max",
  messages = [
    {"role" : "system" , "content" : "你是一个AI助理，回答很简洁!"},
    {"role" : "user" , "content" : "小明有5条宠物狗"},
    {"role" : "assistant" , "content" : "好的"},
    {"role" : "user" , "content" : "小红有3条宠物猫"},
    {"role" : "assistant" , "content" : "好的"},
    {"role" : "user" , "content" : "一共有几条宠物"}
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