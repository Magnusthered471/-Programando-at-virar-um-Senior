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

# introdução da condicionais
read T

if [[ $T == "Y" || $T == "y" ]]; then
  echo "YES"
elif [[ $T == "N" || $T == "n" ]]; then
  echo "NO"
fi

# Mais sobre condicionais
read a b c
if ((a == b && b == c)); then
  echo EQUILATERAL
elif ((a == b || b == c || c == a)); then
  echo ISOSCELES
else
  echo SCALENE
fi


