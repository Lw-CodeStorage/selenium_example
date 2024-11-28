
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 由於不確定假瀏覽器版本，使用自動辨識的方式
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Edge()
# driver.get("https://www.google.com/finance/?sca_esv=ead86818698e8678&sxsrf=ADLYWILM4h7hRlTLXMW9XkcftxWqBQ9kUg:1732372774287&ei=JulBZ7mcEd6ivr0PiK3v-AQ&ved=0ahUKEwi5x9G-1_KJAxVeka8BHYjWG08Q4dUDCA8&uact=5&oq=0050&gs_lp=Egxnd3Mtd2l6LXNlcnAiBDAwNTAyEhAjGIAEGCcYigUYnQIYRhj6ATIKECMYgAQYJxiKBTIIEAAYgAQYsQMyCBAAGIAEGLEDMgUQABiABDIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMhwQABiABBiKBRidAhhGGPoBGJcFGIwFGN0E2AEBSKAHUPsEWPsEcAF4AJABAJgBO6ABO6oBATG4AQPIAQD4AQGYAgKgAkLCAhUQIxiABBiwAxgnGIoFGJ0CGEYY-gHCAg0QIxiABBiwAxgnGIoFwgILEAAYgAQYsAMYsQPCAgkQABiwAxgHGB6YAwCIBgGQBgq6BgYIARABGBOSBwEyoAeNCQ&sclient=gws-wiz-serp&sa=X")

# 自動辨識並安裝
service = Service(executable_path=EdgeChromiumDriverManager().install())

# 啟動 假瀏覽器
driver = webdriver.Edge(service=service)

# 訪問 URL
driver.get('https://www.cwa.gov.tw/V8/C/W/OBS_County.html?ID=64')

# 點擊 高雄的row
driver.find_element(by=By.XPATH, value='//*[@id="stations"]/tr[1]/th/a').click()

# 取得 表格
table = driver.find_element(By.XPATH, value='//*[@id="obstime"]')

# 取得 表格內的全部row
rows = table.find_elements(By.TAG_NAME, 'tr')

result = []
header = ['觀測時間','溫度','天氣','風向','風力','陣風','能見度','相對濕度','海平面氣壓','當日累積雨量','日照時數']

for i, row in enumerate(rows):
    
    temp = {}

    # 取得 表格第一欄時間    
    temp[header[0]] = row.find_element(By.XPATH,value=f'//*[@id="obstime"]/tr[{i+1}]/th').text

    # 取得 各個欄位資料
    tds = row.find_elements(By.TAG_NAME, 'td')

    for j,td in enumerate(tds):
        temp[header[j+1]] = td.text
        # print(td.text)

    result.append(temp)

# 可以將結果透過pandas 存到資料庫
print(result)


# 
# while True:
#     pass


# 以下是一些進階內容整理
# 遍歷同class bane 的資料
# 單個
# news_items = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'yY3Lee')]")
# 多個
# news_items = driver.find_elements(by=By.XPATH, value="//div[contains(@class, 'yY3Lee')]")
# 不斷嘗試到可被訪問，取回多個
# news_items = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'yY3Lee')]")))
# print(news_items)


# 輸入框的操作
# driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/ul[2]/li[2]/a').click()
# account = driver.find_element(by=By.XPATH, value='//*[@id="user_login"]')
# account.clear()
# account.send_keys("abc")

# password = driver.find_element(by=By.XPATH, value='//*[@id="user_password"]')
# password.clear()
# password.send_keys("123")

# password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user_password"]')))
# password.clear()
# password.send_keys("123")


# 下拉選單的操作，需確認是select結構
# from selenium.webdriver.support.ui import Select
# select = Select(driver.find_element_by_name('name'))
# select.select_by_index(index)
# select.select_by_visible_text("text")
# select.select_by_value(value)

# 等待方法
# expected_conditions (通常簡寫為 EC) 提供了多種常見條件：
# presence_of_element_located: 等待元素出現在 DOM 中，但不一定可見。
# visibility_of_element_located: 等待元素出現在 DOM 中，且是可見的。
# element_to_be_clickable: 等待元素可點擊。
# text_to_be_present_in_element: 等待元素中出現指定文字。
# alert_is_present: 等待一個彈窗 (alert) 出現。


# while True:
#     pass