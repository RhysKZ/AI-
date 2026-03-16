import os, json
import uuid

from typing import Sequence
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser

# message_to_dict：单个消息对象 ---> 字典
# messages_from_dict：[字典，字典，字典] ---> [消息对象，消息对象，消息对象]
# AIMessage, HumanMessage, SystemMessage都是BaseMessage的子类

# 步骤1：定义会话历史数据存储类
class FileChatMessageHistory(BaseChatMessageHistory):
  # 步骤1.1：初始化会话历史数据存储类
  def __init__(self, session_id, storage_path):
    self.session_id = session_id        # 会话ID
    self.storage_path = storage_path    # 会话历史数据存储路径

    # 完整的会话历史数据文件路径
    self.file_path = os.path.join(self.storage_path, self.session_id)

    # 确保存储路径存在,如果不存在则创建
    os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

  # 步骤1.2：添加消息到会话历史数据存储类
  def add_message(self, message : Sequence[BaseMessage]) -> None:
    # Sequence序列，类似list列表
    all_messages = list(self.messages)
    all_messages.append(message)

    # 保存会话历史数据到文件
    # 类对象 ---> 字典
    # 列表中的每个元素都是消息对象，需要转换为字典
    # 官方提供message_to_dict：单个消息对象 ---> 字典
    new_messages = [message_to_dict(msg) for msg in all_messages] 
    # 写入文件
    with open(self.file_path, "w", encoding="utf-8") as f:
      json.dump(new_messages,f)

  # 步骤1.3：从会话历史数据存储类中获取所有消息
  # @property装饰器，将方法转换为属性
  @property    
  def messages(self) -> list[BaseMessage]:
    # 从文件中读取会话历史数据，当前文件内：list[字典]
    # 读取文件
    try:
      with open(self.file_path, "r", encoding="utf-8") as f:
        messages = json.load(f)
        return messages_from_dict(messages)
    except FileNotFoundError:
      return []  

  def clear(self) -> None:
    # 清空会话历史数据文件
    with open(self.file_path, "w", encoding="utf-8") as f:
      json.dump([],f)


# 步骤2：定义会话历史数据存储类的实例
model = ChatTongyi(model="qwen3-max")

# 步骤3：定义会话历史数据存储类的实例的提示模板
prompts = ChatPromptTemplate.from_messages([
  ("system", "你是一个厨师，你需要根据会话历史回应用户问题。"),
  MessagesPlaceholder("chat_history"),
  ("human", "{input}"),
])

# 步骤4：定义会话历史数据存储类的实例的输出解析器
src_parser = StrOutputParser()

# 步骤5：定义会话历史数据存储类的实例的链
base_chain = prompts | model | src_parser

# 步骤6：实现通过会话ID从会话历史中获取历史记录的函数
def get_history(session_id):
  return FileChatMessageHistory(session_id, storage_path="./chat_history")


# 步骤7：创建一个新的链，对原有链增强功能：自动附加历史会话
conversation_chain = RunnableWithMessageHistory(
  base_chain,                            # 被增强的原有的chain
  get_history,                           # 通过会话ID从会话历史中获取历史记录的函数
  input_messages_key="input",            # 输入中包含用户问题的占位符
  history_messages_key="chat_history",   # 输入中包含历史会话的占位符
)

# 步骤8：测试会话历史数据存储类的实例的链
if __name__ == "__main__":
  # 固定格式，添加Langchain的配置，为当前程序配置所属的session_id
  session_config = {
    "configurable": {
      "session_id": "8b47074134c34dc08af2ea20b7c9d31b",
    }
  }

# res = conversation_chain.invoke({"input": "小明买了豆腐，可以做什么菜"},session_config)
# print("第一执行")
# print(res)
# res = conversation_chain.invoke({"input": "小红又买了肉沫，可以做什么菜"},session_config)
# print("第二执行")
# print(res)
# res = conversation_chain.invoke({"input": "你再买两样东西，你可以做成出什么菜？"},session_config)
# print("第三执行")
# print(res)
res = conversation_chain.invoke(
  {"input": "那我再买一个整鸡和一棵白菜，除了麻婆豆腐你还还可以做什么菜？"},
  session_config
  )
print("第四执行")
print(res)