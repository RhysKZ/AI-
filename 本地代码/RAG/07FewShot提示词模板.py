from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi


example_prompt = PromptTemplate.from_template("词语：{word}, 反义词：{antonym}")

example_data = [
  {"word": "热", "antonym": "冷"},
  {"word": "大", "antonym": "小"},
  {"word": "快", "antonym": "慢"},
]

few_shot_prompt = FewShotPromptTemplate(
  example_prompt=example_prompt,
  examples=example_data,
  prefix="请根据以下词语和反义词的例子，给出新词语的反义词。",
  suffix="词语：{input_word}, 反义词：",
  input_variables=['input_word']
)

prompt_text = few_shot_prompt.invoke(input={"input_word": "热情"}).to_string()

model = Tongyi(model = "qwen-max")

chain = few_shot_prompt | model
res = chain.invoke(input=prompt_text)
print(res)