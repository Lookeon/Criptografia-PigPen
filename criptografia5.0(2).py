import tkinter as tk
from tkinter import messagebox

criptografia_pigpen = {
    "a": "┘",
    "b": "└┘",
    "c": "└",
    "d": "⊐",
    "e": "□",
    "f": "⊏",
    "g": "┐",
    "h": "┌┐",
    "i": "┌",
    "j": "┘.",
    "k": "└┘.",
    "l": "└.",
    "m": "⊐.",
    "n": "□.",
    "o": "⊏.",
    "p": "┐.",
    "q": "┌┐.",
    "r": "┌.",
    "s": "V",
    "t": ">",
    "u": "<",
    "ú": "<•",
    "v": "Λ",
    "w": "V.",
    "x": ">.",
    "y": "<.",
    "z": "Λ.",

    #Maiúsculas
    "A": "┘⋅⋅",
    "B": "└┘⋅⋅",
    "C": "└⋅⋅",
    "D": "⊐⋅⋅",
    "E": "□⋅⋅",
    "F": "⊏⋅⋅",
    "G": "┐⋅⋅",
    "H": "┌┐⋅⋅",
    "I": "┌⋅⋅",
    "J": "┘⋅⋅⋅",
    "K": "└┘⋅⋅⋅",
    "L": "└⋅⋅⋅",
    "M": "⊐⋅⋅⋅",
    "N": "□⋅⋅⋅",
    "O": "⊏⋅⋅⋅",
    "P": "┐⋅⋅⋅",
    "Q": "┌┐⋅⋅⋅",
    "R": "┌⋅⋅⋅",
    "S": "V⋅⋅",
    "T": ">⋅",
    "U": "<⋅",
    "Ú": "<⋅•",
    "V": "Λ⋅",
    "W": "V⋅⋅",
    "X": ">⋅⋅",
    "Y": "<⋅⋅",
    "Z": "Λ⋅⋅",
    

    #Letras acentuadas
    "Á": "┘⋅⋅•",
    "À": "┘⋅⋅◖",
    "Â": "┘⋅⋅▴",
    "Ã": "┘⋅⋅∿",
    "á": "┘•",
    "à": "┘◖",
    "â": "┘▴",
    "ã": "┘∿",
    "É": "□⋅⋅•",
    "Ê": "□⋅⋅▴",
    "é": "□•",
    "ê": "□▴",
    "Ó": "⊏⋅⋅⋅•",
    "Ô": "⊏⋅⋅⋅▴",
    "Õ": "⊏⋅⋅⋅∿",
    "ó": "⊏•",
    "ô": "⊏▴",
    "õ": "⊏∿",
    "í": "┌•",
    "Í": "┌⋅⋅•",
    "Ç": "└⋅⋅˛",
    "ç": "└˛",
    
    # números
    "0": "┼",
    "1": "┬",
    "2": "┴",
    "3": "├",
    "4": "┤",
    "5": "┌┴",
    "6": "┐┬",
    "7": "└┬",
    "8": "┘┴",
    "9": "╳",

    # símbolos do teclado
    " ": "␣",
    "!": "┘..",
    '"': "┐..",
    "#": "┌..",
    "$": "└..",
    "%": "⊐..",
    "&": "⊏..",
    "'": "┌┐..",
    "(": "└└..",
    ")": "┘┘..",
    "*": "┼..",
    "+": "╪",
    ",": "╶",
    "-": "╴",
    ".": "╵",
    "/": "╱",
    ":": "╸",
    ";": "╹",
    "<": "⊂",
    "=": "⊥",
    ">": "⊃",
    "?": "┐└.",
    "@": "⌂.",
    "[": "⌈",
    "\\": "⌉",
    "]": "⌊",
    "^": "▴.",
    "_": "⎷",
    "`": "◖.",
    "{": "❴",
    "|": "│",
    "}": "❵",
    "~": "∿.",
    "´": "•.",
    "¸": "˛.",
    
}

criptografia_pigpen_inversa = {valor: chave for chave, valor in criptografia_pigpen.items()}

# Flag usada para impedir descriptografia quando o texto original teve 256 caracteres
nao_pode_descriptografar = False

def transcritor_pigpen(texto):
    resultado = []

    for letra in texto:
        resultado.append(criptografia_pigpen.get(letra, letra))

    return " ".join(resultado)


def descriptografador_pigpen(texto):
    partes = texto.split()
    if not partes or not all(parte in criptografia_pigpen_inversa for parte in partes):
        return texto

    resultado = [criptografia_pigpen_inversa[parte] for parte in partes]

    return ''.join(resultado)


def texto_pigpen(texto):
    # Detecta se o texto parece estar criptografado em Pigpen.
    partes = texto.split()
    return bool(partes) and all(parte in criptografia_pigpen_inversa for parte in partes)


# FUNÇÕES DA INTERFACE

def criptografar():
    global nao_pode_descriptografar
    texto = entrada.get()

    if not texto:
        messagebox.showwarning("Aviso", "Digite alguma mensagem.")
        return

    if len(texto) > 256:
        messagebox.showwarning("Aviso", "O texto deve ter no máximo 256 caracteres.")
        caixa_resultado.config(state="normal")
        caixa_resultado.delete(0, tk.END)
        caixa_resultado.config(state="readonly")
        nao_pode_descriptografar = False
        return

    # Verifica se há caracteres não mapeados no dicionário
    caracteres_invalidos = [letra for letra in texto if letra not in criptografia_pigpen]
    if caracteres_invalidos:
        caracteres_unicos = list(set(caracteres_invalidos))
        messagebox.showwarning("Aviso", f"Caracteres não suportados: {', '.join(caracteres_unicos)}")
        return

    nao_pode_descriptografar = len(texto) == 256
    resultado = transcritor_pigpen(texto)

    caixa_resultado.config(state="normal")
    caixa_resultado.delete(0, tk.END)
    caixa_resultado.insert(0, resultado)
    caixa_resultado.config(state="readonly")


def descriptografar():
    global nao_pode_descriptografar
    texto = entrada.get()

    if not texto:
        messagebox.showwarning("Aviso", "Digite alguma mensagem.")
        return

    if nao_pode_descriptografar:
        messagebox.showwarning("Aviso", "Não é possível descriptografar texto criptografado com 256 caracteres.")
        return

    if not texto_pigpen(texto):
        resultado_anterior = caixa_resultado.get().strip()
        if resultado_anterior and texto != resultado_anterior and texto_pigpen(resultado_anterior):
            texto = resultado_anterior
        else:
            messagebox.showwarning("Aviso", "O texto deve estar em Pigpen para descriptografar.")
            return

    resultado = descriptografador_pigpen(texto)

    caixa_resultado.config(state="normal")
    caixa_resultado.delete(0, tk.END)
    caixa_resultado.insert(0, resultado)
    caixa_resultado.config(state="readonly")


def limpar():
    # Limpa os campos de entrada e resultado da interface.
    global nao_pode_descriptografar
    entrada.delete(0, tk.END)
    caixa_resultado.config(state="normal")
    caixa_resultado.delete(0, tk.END)
    caixa_resultado.config(state="readonly")
    nao_pode_descriptografar = False


# JANELA PRINCIPAL DA INTERFACE 

janela = tk.Tk()
janela.title("Pigpen")
janela.geometry("450x220")
background_color = "#31723a"
janela.configure(bg=background_color)

####################################################

# ENTRADA, UMA CAIXA DE TEXTO ONDE VOCÊ ESCREVE A MENSAGEM QUE QUER CRIPTOGRAFAR OU DESCRIPTOGRAFAR
entrada = tk.Entry(
    janela,
    width=45,
    font=("Arial", 11)
)
entrada.pack(pady=15)
####################################################

# BOTÕES
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

# BOTÃO CRIPTOGRAFAR, RESPONSÁVEL POR CHAMAR A FUNÇÃO DE CRIPTOGRAFAR LÁ NO INÍCIO
tk.Button(
    frame_botoes,
    text="Criptografar",
    command=criptografar,
    width=15
).grid(row=0, column=0, padx=5)

# BOTÃO DESCRIPTOGRAFAR, RESPONSÁVEL POR CHAMAR A FUNÇÃO DE DESCRIPTOGRAFAR LÁ NO INÍCIO
tk.Button(
    frame_botoes,
    text="Descriptografar",
    command=descriptografar,
    width=15
).grid(row=0, column=1, padx=5)

# BOTÃO LIMPAR, PARA APAGAR RÁPIDO O TEXTO DE ENTRADA E O RESULTADO
tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar,
    width=15
).grid(row=0, column=2, padx=5)
####################################################

# RESULTADO, CAIXA DE TEXTO QUE MOSTRA O RESULTADO DA CRIPTOGRAFIA/DESCRIPTOGRAFIA
caixa_resultado = tk.Entry(
    janela,
    width=45,
    font=("Arial", 11),
    state="readonly"
)
caixa_resultado.pack(pady=20)
####################################################


# JANELA MAINLOOP, RESPONSÁVEL POR MANTER A JANELA DA INTERFACE ABERTA
janela.mainloop()