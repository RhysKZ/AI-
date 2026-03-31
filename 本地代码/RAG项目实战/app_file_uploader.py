"""
基于StrStreamlit的网页上传服务
file_uploader(
label提示词
type文件类型
accept_multiple_files 是否接受多个文件上传
) 上传文件的组件

"""
import streamlit as st
from knowledge_data_base import KnowledgeBaseService
import time

import config_data

# 标题
st.title("知识库更新服务")

# 上传文件 file_uploader
uploader_file = st.file_uploader(
    "请上传文件",
    type = config_data.file_type,
    accept_multiple_files = False,
)

# st.session_state 就是一个字典
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploader_file is not None:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024

    st.subheader(f"文件名: {file_name}")
    st.write(f"文件类型: {file_type} | 文件大小：{file_size :.2f} KB")

    # 提取文件内容 通过getvalue()方法 获取bytes类型的内容 再使用decode()方法解码为字符串
    text = uploader_file.getvalue().decode("utf-8")

    spinner_placeholder = st.empty()
    spinner_placeholder.info("正在上传文件...")
    time.sleep(2)
    result = st.session_state["service"].upload_by_str(text, file_name)
    spinner_placeholder.empty()
    st.write(result)
