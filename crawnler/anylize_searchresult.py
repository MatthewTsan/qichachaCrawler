# encoding:utf-8

from bs4 import BeautifulSoup
import main
import sys

def get_company(keyword, str):
    result = []
    soup = BeautifulSoup(str, "html5lib")

    # 判断是否被墙
    # 判断是否被墙
    str_ = soup.getText()
    q_str = '''window.location.href='http://www.qichacha.com/index_verify'''
    q_str2 = "window.location.href='https://www.qichacha.com/index_verify"

    if (q_str in str_) or (q_str2 in str_):
        # print('str_ = ', str_)
        print("##########在检索时被墙了##########")
        print("被墙的关键词：", keyword)
        sys.exit(-1)

    login_request_list = soup.find_all("div", attrs={"class":"company-vip-kuang"})
    if len(login_request_list) != 0:
        # print('str_ = ', str_)
        print("##########在检索时被墙了##########")
        print("被墙的关键词：", keyword)
        sys.exit(-1)


    search_list = soup.find_all("section", id="searchlist")
    if len(search_list) == 0:
        return []
    search_table = search_list[0].table
    search_result_list = search_table.find_all("tbody")[0].find_all("tr")
    for item in search_result_list:
        search_result_td = item.find_all("td")

        href = search_result_td[2].a.attrs["href"]
        company_name = search_result_td[2].a.getText()
        result.append([href, company_name])
    return [keyword, result]

def get_total_number(keyword, str):
    soup = BeautifulSoup(str, "html5lib")

    # 判断是否被墙
    q_str = "window.location.href='https://www.qichacha.com/index_verify"
    q_str2 = "window.location.href='http://www.qichacha.com/index_verify"

    if (q_str in str) or (q_str2 in str):
        print("##########在检索时被墙了##########")
        print("被墙的关键词：", keyword)
        sys.exit(-1)

    login_request_list = soup.find_all("div", attrs={"class":"company-vip-kuang"})
    if len(login_request_list) != 0:
        # print('str_ = ', str_)
        print("##########在检索时被墙了##########")
        print("被墙的关键词：", keyword)
        sys.exit(-1)

    result = 1
    page_number_limit = int(main.get_conf("page_number_limit"))

    page_number_part = soup.find_all("div", attrs={
        "class":"text-left m-t-lg m-b-lg"
    })[0].find_all("ul")[0].find_all("a",
                                    attrs={"id":"ajaxpage"})
    if len(page_number_part) == 0:
        return 1
    page_number = page_number_part[-1].string
    if(">" in page_number):
        page_number = page_number_part[-2].string
    page_number = page_number.replace("...", "").strip()
    page_number = int(page_number)
    # print("该关键词的页面数：", min(page_number_limit, page_number), sep=" ")
    return min(page_number_limit, page_number)




if __name__ == '__main__':
    keyword = "周亚武 保定市"
    file = open("test.html","r", encoding="utf-8")
    str = file.read()
    company_result = get_company(keyword, str)
    print(company_result)