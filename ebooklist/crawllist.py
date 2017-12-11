# import sys
# import io
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import csv
# import time

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

def aladin_book(id, pw):
    import sys
    import io
    import requests
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    import csv
    import time

    aladin_list = []
    # Headless Chrome WebDriver 이용하기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome('/Users/jace/bin/chromedriver', chrome_options=options)
    # driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/bin/phantomjs')
    driver.implicitly_wait(3)
    driver.get("https://www.aladin.co.kr/login/wlogin_popup.aspx")
    driver.implicitly_wait(5)
    page = BeautifulSoup(driver.page_source, "html.parser")
    # 알리딘 로그인
    element_id = driver.find_element_by_name("Email")
    element_password = driver.find_element_by_name("Password")
    driver.find_element_by_xpath('//*[@id="LoginForm"]/div/input').click()
    element_id.send_keys(id)
    element_password.send_keys(pw)
    # element_password.send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="LoginForm"]/*[@class="left1_right"]').click()
    try:
        alert = driver.switch_to_alert()
        alert.accept()
    except:
        pass

    page_number = 1
    book_count = 0
    while True:
        time.sleep(3)
        book_list_page = "https://www.aladin.co.kr/account/wmaininfo.aspx?pType=EBookOrders&page="+str(page_number)
        driver.get(book_list_page)
        page = BeautifulSoup(driver.page_source, "html.parser")
        # 목록 테이블 찾기
        if page.find("form", {"id": "frmEBook"}) is None:
            break
        books = page.find("form", {"id": "frmEBook"}).find("tbody").findAll("tr", recursive=False)
        del books[0]

        if len(books) and page_number == 1:
            # 목록 정리
            for book in books:
                # 세트 묶음 처리
                if book.find("td", {"class": "set_t"}):
                    set_title = book.find("td", {"class": "td_gift myacc_td05"}).find("a").get_text()
                    set_link = book.find("td", {"class": "td_gift myacc_td05"}).find("a")["href"]
                    # print("set :", set_title, set_link)
                    set_books = book.find("div", {"class": "list_area"}).findAll("td", {"class": "set_t"})
                    for set_book in set_books:
                        book_info = set_book.find("div", {"class": "ebook_set_layer2"})
                        book_title = set_book.find("a").get_text()
                        book_getdate = book.find("td", {"class": "td_date myacc_td03"}).get_text()
                        book_link = set_book.find("a")["href"]
                        book_count += 1
                        aladin_list.append({'store': "알라딘", 'title': book_title, 'buydate': book_getdate, 'link': book_link})

                # 책 정보 확인
                else:
                    book_info = book.find("td", {"class": "td_gift myacc_td05"})
                    book_title = book.find("a").get_text()
                    book_getdate = book.find("td", {"class": "td_date myacc_td03"}).get_text()
                    book_link = book.find("a")["href"]
                    book_count += 1
                    aladin_list.append({'store': "알라딘", 'title': book_title, 'buydate': book_getdate, 'link': book_link})
            page_number += 1
        else:
            break

    driver.close()
    return aladin_list

def main():
    print(aladin_book('id','pw'))

if __name__ == "__main__":
    main()
