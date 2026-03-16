from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./资料/数据资料/stu.csv",
    csv_args = {
        "delimiter": ","       # 指定分隔符
        "quotechar": '"',       # 指定带有分隔符文本的引号包围是单引号还是双引号
        # 如果数据原本有表头，就不要下面的代码，如果没有可以使用
        "fieldnames": ['name', 'age', 'gender', '爱好']
    },
    encoding="utf-8"
)

# 批量加载 .load()   ->  [Document, Document, ...]
# documents = loader.load()
# for document in documents:
    # print(document)

# 懒加载
for document in loader.lazy_load():
    print(document)


