import base64

def node(url):
    #定义爬取节点函数
    #导入模块
    import requests
    haders = {
'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; PBFT00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36'}
    html=requests.get(url).text
    d = base64.b64decode(html)
    return d
    

a = int(input('请问有几个订阅链接:'))
b = []
while a >0:
    a -= 1
    agr = input('请输入链接')
    b.append(agr)

for i in b:
    url =i
    l = node(url)
    l = str(l)
	
with open("/storage/emulated/0/a节点/爬虫节点.txt","w") as file:
	    file.write(l)
print('成功')

