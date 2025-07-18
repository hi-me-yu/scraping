import requests, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.support.ui import Select


url = "https://www.kaigokensaku.mhlw.go.jp/27/index.php"
option = Options()
driver = webdriver.Chrome(options=option)
driver.get(url)

search_care = driver.find_element(By.LINK_TEXT, "介護事業所を検索する")
search_care.click()

search_button = driver.find_element(By.ID, "osusumeMenu2")
search_button.click()

checkbox_care = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='1']")
checkbox_care.click()

city_link = driver.find_element(By.PARTIAL_LINK_TEXT, "市区町村名から探す")
city_link.click()

checkbox_city = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='272299']")
checkbox_city.click()

last_search = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.btn-search.searchButton")
last_search.click()


address = []

for x in range(page_length):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jigyosyoAddress"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    for y in soup.find_all(class_="jigyosyoAddress"):
        text = y.get_text(strip=True)
        address.append(text)
        
    next = WebDriverWait(driver,10).until(
        EC.find.presence_of_elemnt_located(By.XPAHT, '//a[contains(text(), "次へ")]/..'
    ))
    a_next = driver.find_element(By.XPATH, '//a[contains(text(), "次へ")]/..')
    a_next.get_attribute()
    if "disabled" in next.get_attribute("class"):
        break
        
    if x < page_length:
        old_page_num = driver.find_element(By.CSS_SELECTOR, "ul.pagination li.active").text


        next_btn = WebDriverWait(driver, 10).until(
            EC.find.presence_to_be_clickable((By.XPATH, '//a[contains(text(), "次へ")]'))
        )
        next_btn.click()

        # ページ番号が変わるまで待機
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.CSS_SELECTOR, "ul.pagination li.active").text != old_page_num
        )
        time.sleep(3)  # 少しだけ余裕をもたせる
        
        ＯＫ！！！！！！　でもやっぱり怪しい
# for x in range(page_length):
#     old_address = driver.find_elements(By.CLASS_NAME, "jigyosyoAddress")
    
#     WebDriverWait(driver, 10).until(
#     # EC：seleniumライブラリのモジュールの一つ。●●になったら処理を始めるよ！の条件の集合体
#     EC.presence_of_element_located((By.CLASS_NAME, "jigyosyoAddress"))
# )
#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")
#     for y in soup.find_all(class_= "jigyosyoAddress"):
#         text = y.get_text(strip=True)
#         address.append(text)
    
#     if x < page_length -1 :
#         next_btn = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "次へ")]'))
#     )
#         next_btn.click()
        
#         WebDriverWait(driver, 10).until(
#         lambda d: d.find_elements(By.CLASS_NAME, "jigyosyoAddress") != old_address
#         )
       
# WebDriverWait(操作しているドライバ（edge？chrome？）, 何秒待つか).until( 条件 )→条件が満たされるまで●●秒待つ
# # Javascriptは表示されるのに時間かかるから
# WebDriverWait(driver, 10).until(
#     # EC：seleniumライブラリのモジュールの一つ。●●になったら処理を始めるよ！の条件の集合体
#     EC.presence_of_element_located((By.CLASS_NAME, "jigyosyoAddress"))
# )
# WebDriverWait(driver, 10).until(
#     # EC：seleniumライブラリのモジュールの一つ。●●になったら処理を始めるよ！の条件の集合体
#     EC.presence_of_element_located((By.CLASS_NAME, "page-link"))
# )
# page_source:今見えているブラウザのHTMLを取得する（BeautifulsoupだとJSで追加したテキストなどは取得できない）
# address = [x.get_text(strip=True) for x in soup.find_all(class_="jigyosyoAddress")]

print(address)


# ✅ ここで待機（ブラウザ確認用）
input("処理完了。画面を閉じるにはEnterを押してください。")
driver.quit()

# # MAX_TEXT = 10
# url_request = requests.get(url)

# soup = BeautifulSoup(html, "html.parser")

# # # ◎居宅名
# # # name = [x.get_text(strip=True) for x in soup.find_all(class_="noLink")]

# # # # ◎TEL
# # # tel =class telNumber

# # # # ◎郵便番号
# # # post_code =
# # # class = postalCode
 
# # # # ◎住所
# address = [x.get_text(strip=True) for x in soup.find_all(class_="jigyosyoAddress")]
# # # address = driver.find_elements(By.CLASS_NAME,"jigyosyoAddress")
# # # address_list = [x.text for x in address]


    
    
# # # class = jigyosyoAddress
# # # # ◎提供地域
# # # region = 
# # # class = serviceArea

# print(address)
    
