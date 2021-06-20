
import ply.lex as lex

# Lista de palabras reservadas
reserved = {

    'if' : 'IF',
    'else' : 'ELSE',
    'final' : 'FINAL',
    'in': 'IN',
    'is': 'IS',
    'while' : 'WHILE',
    'for': 'FOR',
    'fun': 'DEF',
    'val': 'VAL',
    'var': 'VAR',
    'Boolean': 'BOOLEAN',
    'Integer': 'INTEGER',
    'null': 'NULL',
    'true': 'TRUE',
    'false': 'FALSE',
    'this': 'THIS',
    'object': 'OBJECT',
    'package': 'PACKAGE',
    'return': 'RETURN',
    'super': 'SUPER',
    'throw': 'THROW',
    'try': 'TRY',
    'enum': 'ENUM',
    'do': 'DO',
    'List': 'LIST',
    'MutableList': 'MUTABLE_LIST',
    'MutableSet': 'MUTABLE_SET'

}

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
    'COMILLASIMPLE',
    'COMILLADOBLE',
    'ID',
) + tuple( reserved.values() )

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
t_COMILLASIMPLE = r'\''
t_COMILLADOBLE = r'\"'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):

    r'[A-z_]\w*'
    t.type = reserved.get(t.value, 'ID')

    return t

def t_error(t):
    
    print("Carácter no permitido '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

def getTokens(lexer):

    while True:
    
        tok = lexer.token()
    
        if not tok:
            break
    
        print(tok)

lexer = lex.lex()
linea = " "

while linea != "":

    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)

print("Ejecución terminada")
