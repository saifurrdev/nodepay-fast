#!/usr/bin/python3.12
# dev : Saifur Rahman Siam
# donate usdt/bep20: 0xec46a2c4b1d00d6aa6d49d4da6354406645d46bb
import requests,time,random,os
import cloudscraper,uuid
from concurrent.futures import ThreadPoolExecutor as tred
os.system('clear')
print("""
Devoloper  :  Siafur Rahman Siam
Youtube    :  @nbprg (Yt)
Tools      :  Nodipay Mining
-----------------------------------""")
_in = input('Put Auth Token :\033[1;32m ')
#os.system('xdg-open https://t.me/cryp2xyz')
print('\033[0m-----------------------------------')
reqx = {
    "ses": "https://api.nodepay.ai/api/auth/session",
    "png": "http://nw.nodepay.ai/api/network/ping"
}
user_id = None
def all_req(local_proxies):
  global _in,user_id
  for proxy in local_proxies:
    try:
        headers = {
        "Authorization": f"Bearer {_in}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://app.nodepay.ai",
        }
        url = reqx['ses']
        scraper = cloudscraper.create_scraper()
        if user_id == None:
             response = scraper.post(url, json={}, headers=headers, timeout=5).json()
             #print(response)
             user_id = response['data']['uid']
        data = {
            "id": user_id,
            "browser_id": str(uuid.uuid4()),
            "timestamp": int(time.time())
        }
        url = reqx['png']
        response = scraper.post(url, json=data, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=5).json()
        #print(response)
        if int(response['code']) == 0:
             print(f"\033[0m[\033[1;32mSuccessful\033[0m]\033[0m Ping Sussess \033[1;32m> \033[0mip score \033[0;31m: \033[1;32m{response['data']['ip_score']}% ")
        #print(response)
    except Exception as e:
        pass

with tred(max_workers=70) as crack:
   local_proxies = open('proxy.txt','r').read().splitlines()
   if int(len(open('proxy.txt','r').read())) < 7:
          exit('Proxy None in : proxy.txt ')
   for x in range(10000000):crack.submit(all_req,local_proxies)
