#引入包
from urllib.request import urlopen

response = urlopen("http://172.29.7.230:8000/share/")

# response = urlopen("http://fund.eastmoney.com/fund.html")
html = response.read();

#这个网页编码是gb2312
#print(html.decode("gb2312"))

#把html内容保存到一个文件
with open("1.txt","wb") as f:
    f.write(html.decode("gb2312").encode("utf8"))
    f.close()