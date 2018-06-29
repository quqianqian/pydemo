from bs4 import BeautifulSoup
import urllib.request
from urllib import error

test_url = "https://www.baidu.com"
proxy_url = "http://www.xicidaili.com/nn/1"
ip_file = "availableIP.txt"


# 保存文件
def write_file(available_list):
    try:
        with open(ip_file, "w+") as f:
            for availabled_ip in available_list:
                f.write(availabled_ip+"\n")
    except OSError as reason:
        print(str(reason))


# 过滤可以使用的IP
def available_ip(ip_list):
    availabled_ip_list = []
    count = 0
    for ip in ip_list:
        count = count + 1
        if count > 10:
            break
        proxy = {"http": ip}
        try:
            handler = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)
            test_resp = urllib.request.urlopen(test_url)
            if test_resp.getcode() == 200:
                availabled_ip_list.append(ip)
        except error.HTTPError as reason:
            print(str(reason))
    return availabled_ip_list


# 抓取网页中的IP
def catch_ip():
    ip_list = []
    try:
        headers = {
            "Host": "www.xicidaili.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
        }
        req = urllib.request.Request(proxy_url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=50)
        content = resp.read()
        soup = BeautifulSoup(content, 'html.parser')
        catch_list = soup.find_all('tr')[1:]

        for i in catch_list:
            td = i.find_all('td')
            ip_list.append(td[1].get_text()+":"+td[2].get_text())
        return ip_list
    except urllib.error.URLError as reason:
        print(str(reason))


# 开始抓取数据
def catch_now():
    print("start catch page ...")
    xi_ci_ip_list = catch_ip()
    print("start test for catch page ...")
    available_ip_list = available_ip(xi_ci_ip_list)
    print("start store for catch page ...")
    write_file(available_ip_list)
    print("end catch ...")


if __name__ == '__main__':
    catch_now()

