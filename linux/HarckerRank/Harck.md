# 📘 Estudo de Linux & Shell Script

## 🌱 Introdução
- Linux é um sistema operacional baseado em Unix.
- Shell é o interpretador de comandos (ex: Bash, Zsh, Sh).
- Shebang (`#!/bin/bash` ou `#!/bin/sh`) define qual shell vai interpretar o script.

## 🖥️ Comandos básicos
- `echo` → imprime texto na tela.
- `pwd` → mostra o diretório atual.
- `ls` → lista arquivos e pastas.
- `cd` → muda de diretório.
- `cat` → mostra o conteúdo de arquivos.

## 🔄 Estruturas de controle
- `for` → repete ações em uma lista ou sequência.
- `while` → repete enquanto a condição for verdadeira.
- `if` → executa comandos se a condição for verdadeira.

## 📂 Exemplos práticos
### Exemplo 1 — Saudação
```bash
#!/bin/bash
read name
echo "Welcome $name"
