# encoding:utf-8

import re
from bs4 import BeautifulSoup
import open_url
import util.util
import output
import time
import sys

def list2str(list):
    str_ = '' + list[0]
    for item in list[1:]:
        str_ = str_ + '|' + item
    return str_

def result_remove_blank(list_to_test):
    for x, item in enumerate(list_to_test):
        if isinstance(item, list):
            result_remove_blank(item)
        else:
            if item is not None:
                str_result = item.strip()
                pattern = re.compile("\s")
                str_result = re.sub(pattern, "", str_result)
                pattern = re.compile("\\x06\\x06")
                str_result = re.sub(pattern, " ", str_result)
                list_to_test[x] = str(str_result)

def get_detail(keyword, name, str_parameter):
    result = []
    result.append(keyword)
    soup = BeautifulSoup(str_parameter, "html5lib")

    # 判断是否被墙
    str_ = soup.getText()
    q_str = '''window.location.href='http://www.qichacha.com/index_verify'''
    q_str2 = "window.location.href='https://www.qichacha.com/index_verify"

    if (q_str in str_) or (q_str2 in str_) :
        print("##########在获取详细信息时被墙了##########")
        print("被墙的关键词：", keyword, name, sep=" ")
        sys.exit(-1)

    # 第一部分数据
    table_company_top = soup.find_all("div", id="company-top")

    dict = {
        "company_name": "暂无",
        "company_tel": "暂无",
        "company_tel_more": "暂无",
        "company_mail": "暂无",
        "company_web": "暂无",
        "company_address": "暂无"
    }

    company_top_content = soup.find_all("div", attrs={"class": "content"})
    # print(company_top_content[0])

    company_top_content_number_rowsIn = 0
    company_top_content_rows = company_top_content[company_top_content_number_rowsIn].find_all("div", attrs={"class": "row"})
    while company_top_content_rows == []:
        company_top_content_number_rowsIn += 1
        company_top_content_rows = company_top_content[company_top_content_number_rowsIn].find_all("div", attrs={"class": "row"})
    # company_name = company_top_content[0].find_all("div", attrs={"class": "row title"})[0]
    # if len(company_name.find_all("h1")) != 0:
    #     company_name = company_name.h1.string
    # else:
    #     company_name = company_name.getText()
    dict["company_name"] = name
    for item in company_top_content_rows:
        if not (len(item.attrs["class"]) == 1):
            continue
        company_top_content_rows_cdes = item.find_all("span", attrs={"class": "cdes"})
        company_top_content_tows_cvlu = item.find_all("span", attrs={"class": "cvlu"})
        for i in range(len(company_top_content_rows_cdes)):
            first = company_top_content_rows_cdes[i].string.replace("：", "")
            second = company_top_content_tows_cvlu[i]
            if "暂无" in second.getText():
                continue
            if "电话" in first:
                company_tel = second.span.string
                dict["company_tel"] = company_tel
            if "官网" in first:
                if "webauth" in second.attrs["class"]:
                    company_web = second.find_all("a")
                    company_web = company_web[0].attrs['href']
                if "cvlu" in second.attrs["class"]:
                    company_web = second.find_all("a")
                    company_web = company_web[0].attrs["href"]
                dict["company_web"] = company_web
            if "邮箱" in first:
                company_mail = second.a.string
                dict["company_mail"] = company_mail
            if "地址" in first:
                company_add = second.a.string
                dict["company_address"] = company_add


    result.append(dict["company_name"])
    result.append(dict["company_tel"])
    result.append(dict["company_tel_more"])
    result.append(dict["company_mail"])
    result.append(dict["company_web"])
    result.append(dict["company_address"])

    # 第二部分数据
    company_info = soup.find_all("section", id="Cominfo")

    company_bossname = company_info[0].find_all("a", attrs={"class":"bname"})
    if len(company_bossname) == 0:
        company_bossname = company_info[0].find_all("div", attrs={"class" : "boss-td"})[0]
        if company_bossname.find_all("a") == 0:
            company_bossname = company_bossname.string
        else:
            company_bossname = company_bossname.a.string
    else:
        company_bossname = company_bossname[0].string
    result.append(company_bossname)

    company_info_ntable = company_info[0].find_all("table", attrs={"class": "ntable"})
    company_info_detail = company_info_ntable[1]

    company_info_detail_tr = company_info_detail.find_all("tr")
    company_business_state = company_info_detail_tr[1].find_all("td")[1].string
    result.append(company_business_state)
    company_start_date = company_info_detail_tr[1].find_all("td")[3].string
    result.append(company_start_date)
    company_socialcreditcode = company_info_detail_tr[2].find_all("td")[1].string
    result.append(company_socialcreditcode)
    company_taxpayercode = company_info_detail_tr[2].find_all("td")[3].string
    result.append(company_taxpayercode)
    company_registrationnumber = company_info_detail_tr[3].find_all("td")[1].string
    result.append(company_registrationnumber)
    company_organizationcode = company_info_detail_tr[3].find_all("td")[3].string
    result.append(company_organizationcode)
    company_type = company_info_detail_tr[4].find_all("td")[1].string
    result.append(company_type)
    company_industry = company_info_detail_tr[4].find_all("td")[3].string
    result.append(company_industry)
    company_place = company_info_detail_tr[6].find_all("td")[1].string
    result.append(company_place)
    company_period = company_info_detail_tr[8].find_all("td")[3].string
    result.append(company_period)

    # print(result)

    company_sockinfo = soup.find_all("section", id="Sockinfo")
    if len(company_sockinfo) == 0:
        company_sockinfo_list = "没有信息"
    else:
        company_sockinfo = company_sockinfo[0].table
        company_sockinfo_detail = company_sockinfo.find_all("tr")
        company_sockinfo_list = []
        for line in company_sockinfo_detail[1:]:
            # print("linex: ", line, end="\n\n")
            table_in = line.find_all("table")
            if len(table_in) == 0:
                continue
            if ("class" in line.contents[1].attrs):
                if (line.contents[1].attrs["class"] != ['tx']):
                    continue
            company_sockinfo_detail_td = line.find_all("td")
            company_sockinfo_name_table = company_sockinfo_detail_td[1].table
            company_sockinfo_name = company_sockinfo_name_table.find_all("h3")[0].string

            company_sockinfo_percent = line.find_all("td", attrs="text-center")[0].string
            company_sockinfo_list.append(company_sockinfo_name.strip() + "+" + company_sockinfo_percent.strip())
    result.append(list2str(company_sockinfo_list))

    company_mainmember_table = soup.find_all("section", id="Mainmember")
    if len(company_mainmember_table) == 0:
        company_mainmember_list = ["没有结果"]
    else:
        company_mainmember_table = company_mainmember_table[0].table
        company_mainmember_table_tr = company_mainmember_table.find_all("tr")
        company_mainmember_list = []
        for line in company_mainmember_table_tr[1:]:
            company_mainmember_table_td = line.find_all("td")
            company_mainmember_name = company_mainmember_table_td[1].find_all("a")[0].string
            company_mainmember_position = company_mainmember_table_td[2].string
            company_mainmember_list.append(company_mainmember_name.strip() + "+" + company_mainmember_position.strip())
    result.append(list2str(company_mainmember_list))

    company_change_list = []
    company_change_table = soup.find_all("section", id="Changelist")
    if len(company_change_table) == 0:
        company_change_list.append(["暂无","", "", ""])
    else:
        company_change_table = company_change_table[0].table
        company_change_table_tr = company_change_table.find_all("tr")
        for line in company_change_table_tr[1:]:
            company_change_table_td = line.find_all("td")
            str_before_change = company_change_table_td[3].div.getText()
            str_before_change.replace("<em>", "")
            str_before_change.replace("</em>", "")
            str_before_change.replace("<br>", "")
            str_after_change = company_change_table_td[4].div.getText()
            str_after_change.replace("<em>", "")
            str_after_change.replace("</em>", "")
            str_after_change.replace("<br>", "")
            # print(str_before_change, str_after_change, sep=" ")
            if ("【退出】" in str_before_change) or ("【退出】" in str_after_change) or ("【新增】" in str_before_change) or ("【新增】" in str_after_change):
                str_change_date = company_change_table_td[1].string
                str_change_item = company_change_table_td[2].getText()
                # str_change_item.replace("<br>", "")
                # str_change_item.replace('<span class="text-gray" style="font-size: 12px">', "")
                # str_change_item.replace("</span>", "")
                company_change_list.append([str_change_date, str_change_item, str_before_change, str_after_change])
    if len(company_change_list) == 0:
        company_change_list.append(["暂无", "", "", ""])
    result.append(company_change_list)
    # result.append("变更信息")

    risk_list = []
    risk_list.append("风险提示")
    # company_risk = soup.find_all("div", attrs={"class":"risk-panel b-a"})
    # company_risk_url = company_risk[0].find_all("a")
    # if len(company_risk_url) == 0:
    #     risk_list.append("暂无")
    # else:
    #     company_risk_url = company_risk_url[1].attrs["href"]
    #     if company_risk_url.strip()[0] == "/":
    #         company_risk_url = util.util.qichacha_Url + company_risk_url.strip()
    #     risk_page_str = open_url.open_url(company_risk_url)
    #     soup_risk_page = BeautifulSoup(str)
    #     soup_risk_title = soup_risk_page.find_all("div", attrs={"class":"rick-sell"})
    #     for item in soup_risk_title:
    #         risk_list.append(item.string.strip())

    result.append(list2str(risk_list))

    result_remove_blank(result[1:])
    print(result)
    return result

if __name__ == '__main__':
    # str_from_url = open_url.open_url("https://www.qichacha.com/firm_03886915db29fa6e68f1165e19dcc0d2.html")
    f = open("test.html", "r", encoding="utf-8")
    str_from_file = f.read()
    print(get_detail("洪福骏股份有限公司", "洪福骏股份有限公司", str_from_file), sep="\n")