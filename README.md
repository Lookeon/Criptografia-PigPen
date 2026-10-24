# Criptografia Pigpen

Projeto de estudo baseado na cifra Pigpen, originalmente feita em papel, adaptado para uso em um dispositivo eletrônico. O programa tem uma interface gráfica simples onde é possível criptografar e descriptografar mensagens.

## Funcionalidades

- Criptografar textos para símbolos Pigpen
- Descriptografar textos que estejam em Pigpen
- Suporte a letras maiúsculas e minúsculas, letras acentuadas, números e símbolos do teclado
- Aviso quando o texto contém caracteres não suportados
- Botão para limpar os campos rapidamente

## Tecnologias

- Python 3
- Tkinter (já vem instalado com o Python na maioria dos sistemas)

## Como executar

1. Instale o [Python 3](https://www.python.org/downloads/)
2. Clone o repositório:
   ```bash
   git clone https://github.com/Lookeon/Criptografia-PigPen.git
   ```
3. Entre na pasta e execute o arquivo:
   ```bash
   cd Criptografia-PigPen
   python criptografia5.0.py
   ```

## Como usar

1. Digite a mensagem no campo de cima
2. Clique em **Criptografar** ou **Descriptografar**
3. O resultado aparece no campo de baixo
4. Use **Limpar** para apagar os dois campos

## Limitações

- O texto deve ter no máximo 256 caracteres
- Textos criptografados com exatamente 256 caracteres não podem ser descriptografados
- Caracteres fora do dicionário de símbolos não são suportados

## Status

Projeto em desenvolvimento, feito para fins de estudo.
