#!/bin/bash
#Corte nº 1 
#Vamos trabalhar do corte de um texto escrevendo sobre a primeira letra de cada palavra.
while read line; do
  echo ${line:2:1}
  done 
