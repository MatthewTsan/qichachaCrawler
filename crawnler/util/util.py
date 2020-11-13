# encoding:utf-8
import time

qichacha_Url = "https://www.qichacha.com"
search_Url = qichacha_Url + "/search?key="

result_file = "result"
locatime = time.strftime("%m%d_%H%M%S", time.localtime())
save_data_name = result_file + "\\result.xlsx"
fail_data_name = result_file + "\\fail.xlsx"



detail_name = ["关键词", "公司名称","电话", "更多号码", "邮箱", "官网", "地址", "法定代表人姓名", "经营状况", "成立日期", "统一社会信用代码",
               "纳税人识别号","注册号","组织机构代码","公司类型","所属行业","所属地区","营业期限","股东姓名及持股比例",
               "主要人员姓名及职务","变更日期","变更项目","变更前","变更后","风险扫描"]

# 只有在变更记录这个位置是一个list[]，其他的都是string
change_list_pos = 20



file_test_name = "测试样本(1).xlsx"
file_sheet_name = "人名+联系方式+所在地"

file_cookie = "cookie.txt"

config_file = "conf.cfg"
config_encode_file = "conf_encode.cfg"