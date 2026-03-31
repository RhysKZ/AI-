"""
知识库
"""

import os
from uuid import main

import config_data as config
import hashlib
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime

# 检查文件是否被处理过
def check_dir(md5_str : str):
    if not os.path.exists(config.md5_path):
        open(config.md5_path, 'w', encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path, 'r', encoding="utf-8").readlines():
            # 处理字符串前后的空格和换行符
            line = line.strip()
            if line == md5_str:
                return True
        return False

# 将md5值追加保存到文件中
def save_md5(md5_str : str):
    with open(config.md5_path, 'a', encoding="utf-8") as f:
        f.write(md5_str + '\n')

# 将传入的字符串转换为md5值
def get_string_md5(input_str : str, encoding='utf-8'):
    """将字符串转换为bytes"""
    str_bytes = input_str.encode(encoding)
    """创建md5对象"""
    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    md5_hex = md5_obj.hexdigest()
    return md5_hex

class KnowledgeBaseService:
    def __init__(self):
        os.makedirs(config.persist_directory, exist_ok=True)

        """初始化向量数据库"""
        self.chroma = Chroma(
            # 集合名
            collection_name = config.collection_name,
            # 嵌入模型
            embedding_function = DashScopeEmbeddings(model = "text-embedding-v4"),
            # 向量数据库的目录
            persist_directory = config.persist_directory,
        )

        """初始化文本分割器"""
        self.spliter = RecursiveCharacterTextSplitter(
            # 分割后的文本段最大长度
            chunk_size = config.chunk_size,
            # 连续分割的文本段之间的重叠长度
            chunk_overlap = config.chunk_overlap,
            # 分割器的分隔符
            separators = config.separators,
            # 使用python自带的len函数做长度统计的依据
            length_function = len,
        )

    def upload_by_str(self, data: str, file_name):
        # 先得到传入的字符串的md5值
        md5_hex = get_string_md5(data)

        if check_dir(md5_hex):
            return "文件已被处理，请勿重复上传"

        if len(data) > config.max_split_char_number:
            knowledge_chunks: list[str] = self.spliter.split_text(data)
        else:
            knowledge_chunks = [data]

        metadata = {
            "source": file_name,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "Rhys",
        }

        self.chroma.add_texts(
            knowledge_chunks,
            metadatas=[metadata for _ in knowledge_chunks],
        )

        save_md5(md5_hex)

        return "文件上传成功"


if __name__ == "__main__":
    service = KnowledgeBaseService()
    by_str = service.upload_by_str("周杰伦", "text")
    print(by_str)



