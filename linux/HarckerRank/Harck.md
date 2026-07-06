# 📘 Estudo de Linux & Shell Script

# 🌱 Introdução
O Linux é um sistema operacional controlado por comandos de texto. Quando criamos um roteiro de tarefas (Script), o "Shell" entra em ação como um tradutor, pegando o que você escreveu e explicando para o computador executar. A primeira linha de um arquivo (`#!/bin/bash` ou `#!/bin/sh`) serve apenas para avisar ao sistema qual é o tradutor que deve ser usado para ler aquele texto.

# 🖥️ Comandos básicos
No terminal, usamos palavras simples no lugar do mouse para mexer no sistema:
- `echo`: Funciona como um alto-falante, apenas exibe uma mensagem na tela.
- `pwd`: É o seu GPS, mostra o caminho exato da pasta onde você está pisando agora.
- `ls`: Abre os seus olhos, listando tudo o que está guardado dentro da pasta atual.
- `cd`: É o seu meio de transporte, serve para entrar ou sair das pastas.
- `cat`: Funciona como uma lupa, joga o texto de um arquivo na tela para você ler rápido.

# 🔄 Estruturas de controle
Para fazer o computador tomar decisões sozinho e automatizar tarefas, usamos três regras lógicas:
- `if` (Se): Faz o sistema tomar uma decisão. Se uma regra for verdadeira, ele faz a ação; se não for, ele ignora.
- `for` (Para cada): Pega uma lista de coisas e faz a mesma ação com cada uma delas, uma por uma, até a lista terminar.
- `while` (Enquanto): Cria uma repetição contínua. O sistema fica fazendo a mesma tarefa sem parar, enquanto a regra continuar sendo verdadeira.

# 📂 Exemplo prático de funcionamento
Imagine um script simples de "Saudação". O computador lê a primeira linha para ativar o tradutor (Bash), depois ele faz uma pausa para ler o que você digitar no teclado (como o seu nome) e, por fim, usa o alto-falante (`echo`) para colar o seu nome junto com uma mensagem de boas-vindas na tela. Tudo de forma automática e sem mistério!