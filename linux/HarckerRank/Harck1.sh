#!/bin/sh
# Usando harckerRank para melhorar o meu conhecimento em shell script

# Primeira lesson do site aprendir sobre Shebang sendo(#!/bin/sh),que fas o script ser interpretado pelo shell, e não por outro interpretador de comandos.

echo "HELLO"
# O echo imprime o qe eu escrevo dentro do "".

read name
# O code read fusiona como um leitor do que eu escrevo no terminal, e o name fusiona como uma variavel que recebe o que e escrevo como em python.
echo "Welcome" $name
# O echo é usado para imprimir o que eu escrevo no terminal, exemplo: echo "Hello World" e o $ serve para revevelar a variavel que eu criei, no caso o name.