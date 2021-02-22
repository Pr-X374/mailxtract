try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
from bs4 import BeautifulSoup
import re , requests



# to search
def find_mail_by_name(name,k,g):
    print("starting google search")
    print("---------------------------------------------------------------------------------------")
    query = name+""" "@orange.fr" """
    head = {'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-G960F '\
                            'Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) '\
                            'Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'}
    for j in search(query, tld="com" , stop=200000, pause=100 , user_agent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F '\
                            'Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) '\
                            'Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'):
        if 'pdf' in j :
            pass
        else :
            url = j
            print(url)
            try:
                r = requests.get(url , headers = head, timeout = 10 )
                code = r.status_code
                if code == 200:
                    soup = BeautifulSoup(r.text, 'lxml')
                    for x in  re.findall(r'[\w\.-]+@orange.fr+', soup.text ) :
                        if x not in k :
                            print(x)
                            g.write(x+'\n')
                            k.append(x)
            except Exception as e:
                print(e)
                pass

    return k


f = open("name.txt", "r")

k = []
g = open("mail list.txt", "a")
for name in f.readlines() :
    k = find_mail_by_name(name,k,g)
g.close()
