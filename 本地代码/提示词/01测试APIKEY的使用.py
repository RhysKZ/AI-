from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "你能做什么"}
    ],
    stream=True
)

for chunk in completion:
    print(chunk.choices[0].delta.content, end="",flush=True)