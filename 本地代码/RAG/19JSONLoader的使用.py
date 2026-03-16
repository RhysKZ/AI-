from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./资料/数据资料/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,
    json_lines=True
)

documents = loader.load()
print(documents)