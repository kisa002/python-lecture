import requests
import pandas as pd
from bs4 import BeautifulSoup

titles = []
writers = []
codes = []

show = False

def search_book(page):
    URL = 'http://hanbit.co.kr/store/books/category_list.html?cate_cd=001001&page=' + str(page)

    response = requests.get(URL)

    html = response.text
    header = response.headers
    status = response.status_code
    is_ok = response.ok

    soup = BeautifulSoup(html, 'html.parser')
    books = soup.select(
        'div > div > ul > li > div > div > p'
    )

    print("-----", page, "PAGE ------")
    is_title = True
    for book in books:        
        if is_title == True:
            titles.append(book.text.replace(',', '，'))
            is_title = False
        else:
            writers.append(book.text.replace(',', '，').strip())
            is_title = True

    books = soup.select(
        'div > div > ul > li > div > div > p > a'
    )
    
    for book in books:
        codes.append(book.get('href').split('code=')[1].strip())

    if show == True:
        for i in range(len(titles)):
            print(titles[i], "-", writers[i], "-", codes[i])

    if page == 1:
        with open("book.csv", "w", encoding="utf-8") as f:
            f.write("제목, 작성자, 코드\n")
        f.close()

    for i in range(len(titles)):
        with open("book.csv", "a", encoding="utf-8") as f:
            f.write(titles[i] + ", " + writers[i] + ", " + codes[i] + "\n")
        f.close()

    soup = BeautifulSoup(html, 'html.parser')
    books = soup.select(
        'div > div > a'
    )

    for book in books:
        if str(page + 1) == book.text:
            search_book(page + 1)
            break
        elif book.text == ">":
            search_book(page + 1)
            break

def show_csv():
    csv_data = pd.read_csv("book.csv")
    csv_data.head()
    print(csv_data)
    
def main():
    menu = int(input("1. 크롤링 - 처리 과정 표시\n2. 크롤링 처리 과정 표시 x\n3. csv 표시\n > "))
    
    if menu == 1:
        global show
        show = True
        search_book(1)
    elif menu == 2:
        search_book(1)
    else:
        show_csv()

main()

