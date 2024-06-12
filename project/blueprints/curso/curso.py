import re

cursos = {}

def validar_codigo(codigo):

    if len(codigo) != 7:
        return False
    if not codigo[:3].isalpha() or not codigo[3:].isdigit():
        return False
    return True


def validar_dados(dados):
    required_keys = ["nome", "duracao"]
    for key in required_keys:
        if key not in dados:
            return False
    return True


def atualizar_curso(codigo, dados):

    if not validar_codigo(codigo):
        return "falha"

    if not validar_dados(dados):
        return "falha"

    for curso in cursos:
        if curso["codigo"] == codigo:
            curso.update(dados)
            return "sucesso"

    return "falha"


def consultar_curso(codigo):
    if not validar_codigo(codigo):
        return "Código de curso inválido"
    for curso in cursos:
        if curso["codigo"] == codigo:
            return curso

    return "Curso não encontrado"

def excluir_curso(codigo):
    if not validar_codigo(codigo):
        return "falha"

    for i, curso in enumerate(cursos):
        if curso["codigo"] == codigo:
            del cursos[i]
            return "sucesso"

    return "falha"

codigo = "XYZ9999"
resultado = excluir_curso(codigo)
print(resultado)

codigo = "ABC1234"
resultado = consultar_curso(codigo)
print(resultado)

codigo = "XYZ9999"
resultado = consultar_curso(codigo)
print(resultado)

codigo = "ABC1234"
resultado = excluir_curso(codigo)
print(resultado)

codigo = "ABC1234"
dados = {"nome": "Curso de Python Avançado", "duracao": "50 horas"}
resultado = atualizar_curso(codigo, dados)
print(resultado)

codigo = "XYZ9999"
dados = {"nome": "Curso de Novo", "duracao": "30 horas"}
resultado = atualizar_curso(codigo, dados)
print(resultado)

codigo = "DEF5678"
dados = {"nome": "Curso de Java Avançado"}
resultado = atualizar_curso(codigo, dados)
print(resultado)
