from bs4 import BeautifulSoup

# 读取文件内容
with open("1.txt", "rb") as f:
    html = f.read().decode("utf8")
    f.close()


# html = render(request, 'index.html').content 
bs = BeautifulSoup(html, "html.parser")
noti_div = bs.find('div', id='header-bottom-right')
print(bs.div)


# # 分析html内容
# soup = BeautifulSoup(html,"html.parser")

# # 取出网页title
# print(soup.title) #<title>每日开放式基金净值表 _ 天天基金网</title>

# # 基金编码
# codes = soup.find("table",id="oTable").tbody.find_all("td","bzdm")

# result = () # 初始化一个元组
# for code in codes:
#     result += ({
#         "code":code.get_text(),
#         "name":code.next_sibling.find("a").get_text(),
#         "NAV":code.next_sibling.next_sibling.get_text(),
#         "ACCNAV":code.next_sibling.next_sibling.next_sibling.get_text()
#      },)



# # 打印结果
# print(result[0]["name"])