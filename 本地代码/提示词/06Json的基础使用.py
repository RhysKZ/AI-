import json

d = {
    "name": "周杰轮",
    "age": 11,
    "gender": "男"
}

s = json.dumps(d,ensure_ascii=False)
print(s)

l = [
    {
        "name": "周杰轮",
        "age": 11,
        "gender": "男"
    },
    {
        "name": "蔡依临",
        "age": 12,
        "gender": "女"
    },
    {
        "name": "小明",
        "age": 16,
        "gender": "男"
    }
]

print(json.dumps(l,ensure_ascii=False))
print("---------------------------------------------------------------------------------------------")
print(json.loads(json.dumps(l,ensure_ascii=False)))
