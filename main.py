import ply.lex as lex

#Parte realizada por Melina Macias
#Definicion de tokens
tokens = (
    'NUMERO',
    'MAS',
    'MULTI',
    'MAYOR',
    'MENOR',
    'LPAREN',
    'RPAREN',
    'RLLAVE',
    'LLLAVE',
    'LCORCH',
    'RCORCH',
    'DOSPUNT',
    'IGUAL',
    'MASIGUAL',
    'DOBLEIGUAL',
)

#ER para tokens definidos
t_MAS = r'\+'
t_MULTI =r'\*'
t_MAYOR =r'\>'
t_MENOR =r'\<'
t_LPAREN =r'\('
t_RPAREN =r'\)'
t_LLLAVE =r'\{'
t_RLLAVE =r'\}'
t_LCORCH =r'\['
t_RCORCH =r'\]'
t_DOSPUNT =r'\:'
t_IGUAL = r'\='
t_MASIGUAL = r'\+='
t_DOBLEIGUAL =r'\={2}'


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Carácter no permitido '%s'" % t.value[0])
    t.lexer.skip(1)


