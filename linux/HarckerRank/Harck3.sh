#!/bin/bash

# Criando um scritp para comparar dois numeros.
read X
read Y
if ((X < Y)); then
  echo X is less than Y
elif ((X > Y)); then
  echo X is greater than Y 
else
  echo X is equal to Y
fi

#Introdução às condicionais
read T

if [[ $T == "Y" || $T == "y" ]]; then
  echo "YES"
elif [[ $T == "N" || $T == "n" ]]; then
  echo "NO"
fi


