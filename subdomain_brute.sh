#!/usr/bin/bash

BLUE='\033[0;34m'

RED='\033[0;31m'

NOCOLOR='\033[0m'



filename="$1" #Arquivo de sub domains

host="$2" #Domínio a ser verificado



if [ "$1" == "" ] || ["$2" == ""]

then

	echo -e "${RED}Informe os argumentos${NOCOLOR}"

	echo "Exemplo:"

	echo "./host_brute.sh lista_de_subdomains.txt dominio.com"

else



echo -e "${BLUE}Realizando força bruta de subdomains..."

while read -r line; do

    subdomain="$line"

    host_sub="$subdomain"."$host"

    out_host=$(host $host_sub)


    #Colocar somente os subdomains validos

    if [[ $out_host != *"not found"* ]]; then

	    #"ACHOU, COLOCA NO ARQUIVO"

	    echo "$host_sub" >> positives.txt

	    echo "$out_host" >> positives.txt

    fi

	

    sleep 1

done < "$filename"

fi
