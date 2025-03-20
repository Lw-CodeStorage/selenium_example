import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 這些建議都加上，不開頁面、禁用GPU加速等等
options = webdriver.EdgeOptions()
options.add_argument("--headless")  # 無頭模式
options.add_argument("--disable-gpu")  # 禁用 GPU 加速
options.add_argument("--disable-extensions")  # 禁用擴展
options.add_argument("--disable-infobars")  # 禁用訊息欄
options.add_argument("--disable-notifications")  # 禁用通知
options.add_argument("--no-sandbox")  # 取消沙盒模式
options.add_argument("--disable-dev-shm-usage")  # 防止資源不足的錯誤
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
)
# 啟動 Edge 瀏覽器
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

# 確認 Edge 版本和驅動版本
print("Edge version:", driver.capabilities["browserVersion"])
print("EdgeDriver version:", driver.capabilities["msedge"]["msedgedriverVersion"])

# 開始使用
driver.get("https://ithelp.ithome.com.tw/articles/10225429")

# 取得頁面標題來測試是否成功加載
print("Page title:", driver.title)

# 關閉瀏覽器
driver.quit()
