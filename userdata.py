import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

def get(key):
    """
    從環境變數中獲取指定的值
    """
    return os.getenv(key) 