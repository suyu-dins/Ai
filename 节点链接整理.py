import base64
import re
      #定义爬取节点函数
def node(url):
    #访问订阅链接
    import requests
    haders = {
'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; PBFT00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36'}
    html=requests.get(url).text
    return html
    
#获取有多少订阅
a = int(input('请问有几个订阅链接👉:'))
b = []
while a >0:
    a -= 1
    agr = input('请输入第个链接👉:')
    b.append(agr)
#循环遍历节点
age=0
nodeon=()
for i in b:
    url = i
    list1=[]
    l = str(node(url))
    d = str(base64.b64decode(l))
    url2=re.findall(r'([vmess|trojan|vless].*?)\\n',d)
    u=tuple(url2)
    nodeon += u
    age += 1
    print(f"第 {age} 个链接已转换成功")
#将元组转换为列表
nodeon=list(nodeon)

#将列表元素换行写入txt文件
with open("/storage/emulated/0/a节点/爬虫节点.txt","w") as fp:
	[fp.write(str(item)+'\n') for item in nodeon]
	fp.close()

#with open("/storage/emulated/0/a节点/爬虫节点.txt","w") as file:
#	    file.write(list_node)
	    
print('全部成功')   
	    
