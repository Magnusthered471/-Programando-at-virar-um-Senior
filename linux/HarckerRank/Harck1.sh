#!/bin/sh
# Usando harckerRank para melhorar o meu conhecimento em shell script

# Primeira lesson do site aprendir sobre Shebang sendo(#!/bin/sh),que fas o script ser interpretado pelo shell, e não por outro interpretador de comandos.

# O echo imprime o qe eu escrevo dentro do "".
echo "HELLO"
# Como escrever meu nme junto com o welcome
read name
echo "Welcome" $name
# Escrevendo do 1 a 50.
for D in {1..50}
do
    echo "Number: $D"
done
# Escrevendo do 1  50 ms em umeros impares.
for D in {1..50..2}
do
    echo "Number: $D"
done
