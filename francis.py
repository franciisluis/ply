# FRANCIS LUIS E ESTER
import sys #fornece funções para interagir com o interpretador e o SO
import re
import ply.lex as lex
cpf="042.225.230-11"
celular ="5199973-7448"
radio= "F.M. 101.2 MHz"

tokens = (
    'CPF',
    'CELULAR',
    'RADIO',
    'MATRICULA',
    'REAIS',
    'TAGS',
    'URL',
    'PALAVRAS',
    'STRINGS',
    'CNPJ',
)

#042.225.230-11
t_CPF = r'^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$'
#re.findall(r"^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$", cpf): EXEMPLO PYTHON NORMAL
#5199973-7448 : EXEMPLO CELULAR
t_CELULAR = r'^[0-9]{1}[0-9]{1}[9]{1}[0-9]{4}[-][0-9]{4}$'
#re.findall(r"^[0-9]{1}[0-9]{1}[9]{1}[0-9]{4}[-][0-9]{4}$",celular):
#F.M. 101.2 MHz
#t_RADIO = r'^[F||A][.][M][.] [8||9||10 - 9]{2,3}[.][1-9] [M][H][z]$'
t_RADIO = r'^([F|A]\.[M]\.\ [0-9]{3}\.[0-9]{1}\ [M][H][z])$'
#152008569-6
t_MATRICULA = r'^[0||1||2|]{1}[0-9]{1}[1||2]{1}[0-9]{6}[-][0-9]{1}$'
#50.0
t_REAIS = r'^[0-9]{1,9}[.][0-9]{1,9}$'
t_TAGS = r'^[<][a-z]{0,100}[>][<][/][a-z]{0,100}[>]$'
#https://google.com
t_URL = r'^(http|ftp|https):\/{2}'
#Palavras
t_PALAVRAS = r' ^[a-z||A-Z]{1,199}'
#"string"
t_STRINGS = r'^["][0-9||a-z||A-Z]{1,199}["]'
#20.654.256/0001-02
t_CNPJ = r'^[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0]{3}[1][-][0-9]{2}$'

# rastrea os numerods das linhas
def t_newline(t):
    t.lexer.lineno += len(t.value)
# Ignorar caracteres de espaço
t_ignore = ' \t'
# Verifica erros
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()
arquivo = open("testeregex.txt", "r")
for token in arquivo:
    lexer.input(token)
    tok = lexer.token()
    print(tok)


