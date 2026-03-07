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
  ]
)

# 3、处理结果
print(response.choices[0].message.content)
print("-------------------------------------------------------------------------------------------")
print(response.choices)

# 输出的结构
# {
#   "Choice": {
#     "finish_reason": "stop",
#     "index": 0,
#     "logprobs": null,
#     "message": {
#       "content": "以下是几种输出数字1-10的Python代码：\n\n## 方法1：使用for循环和range()\n```python\nfor i in range(1, 11):\n    print(i)\n```\n\n## 方法2：使用while循环\n```python\ni = 1\nwhile i <= 10:\n    print(i)\n    i += 1\n```\n\n## 方法3：一行代码输出（用空格分隔）\n```python\nprint(*range(1, 11))\n```\n\n## 方法4：输出在同一行，用逗号分隔\n```python\nprint(\", \".join(map(str, range(1, 11))))\n```\n\n最常用和推荐的是**方法1**，因为它简洁、易读且符合Python的编程风格。\n\n运行方法1的输出结果：\n```\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n```",
#       "refusal": null,
#       "role": "assistant",
#       "annotations": null,
#       "audio": null,
#       "function_call": null,
#       "tool_calls": null
#     }
#   }
# }