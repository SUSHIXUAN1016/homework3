print("測試開始...")

try:
    import google.generativeai as genai
    print("成功導入 google.generativeai")
    
    import os
    print("成功導入 os")
    
    from dotenv import load_dotenv
    print("成功導入 dotenv")
    
    # 載入環境變數
    load_dotenv()
    print("成功載入 .env 文件")
    
    # 獲取 API key
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key:
        print("成功獲取 API key")
    else:
        print("錯誤：無法獲取 API key")
    
    # 配置 Gemini API
    genai.configure(api_key=api_key)
    print("成功配置 Gemini API")
    
    # 創建模型
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("成功創建模型")
    
    # 測試生成內容
    response = model.generate_content("你好")
    print("成功生成內容")
    print(f"回應：{response.text}")
    
except Exception as e:
    print(f"發生錯誤：{str(e)}")

print("測試結束") 