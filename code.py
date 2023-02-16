import requests
def load_page(url):
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    request = requests.get(url, headers=headers)
    return request.text

def save_file(text,i): 
    with open('D:\\Temp\heima%d.html'%(i),mode='w+',encoding='utf-8') as f:   
        f.write(str(text))

def heima_forum(begin_page, end_page):
    for page in range(begin_page, end_page + 1):
        url = f'http://bbs.itheima.com/forum-425-{page}.html'
        file_name = "正在请求第" + str(page) + "页"
        print(file_name)
        html = load_page(url)
        save_file(html,page)

if __name__ == "__main__":
    begin_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    heima_forum(begin_page, end_page)
