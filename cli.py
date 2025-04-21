import google.generativeai as genai
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

def main():
    print("正在初始化...")
    
    # 配置 Gemini API
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    if not GEMINI_API_KEY:
        print("錯誤: GEMINI_API_KEY 環境變數未設置")
        print("請確保 .env 文件存在並包含正確的 API key")
        return

    try:
        print("正在配置 Gemini API...")
        genai.configure(api_key=GEMINI_API_KEY)
        print("正在載入模型...")
        model = genai.GenerativeModel("gemini-1.5-flash")
        print("模型載入成功！")
    except Exception as e:
        print(f"錯誤: 無法初始化 Gemini API - {str(e)}")
        return
    
    print("\n歡迎使用 Gemini AI 聊天機器人 (CLI 模式)")
    print("輸入 'exit' 或 'quit' 來結束對話")
    print("請輸入您的問題：")
    
    while True:
        try:
            user_input = input("\n您: ")
            if user_input.lower() in ['exit', 'quit']:
                print("再見！")
                break
                
            print("正在處理您的問題...")
            response = model.generate_content(user_input)
            print(f"\nAI: {response.text}")
        except KeyboardInterrupt:
            print("\n再見！")
            break
        except Exception as e:
            print(f"\n錯誤: {str(e)}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"發生未預期的錯誤: {str(e)}") 