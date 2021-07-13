
import json
from os import error
import sys
import ply.lex as lex

dumpErrors = []

# Lista de palabras reservadas
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'fun': 'FUN',
    'val': 'VAL',
    'var': 'VAR',
    'Boolean': 'BOOLEAN',
    'Integer': 'INTEGER',
    'Double': 'FLOAT',
    'as': "CASTOPERATOR",
    'String': "STRING",
    'true': 'TRUE',
    'false': 'FALSE',
    'MutableList': 'MUTABLE_LIST',
    'MutableSet': 'MUTABLE_SET',
    'println': 'PRINTLN',
    'readLine': 'READ_LINE',
    'get': 'GET',
    'add': 'ADD',
    'iterator': "GET_ITERATOR",
    'clear': "CLEAR_ALL",
    'mutableListOf': 'MUTABLE_LIST_OF',
    'mutableSetOf': 'MUTABLE_SET_OF',
    'max':'MAX',
    'min': 'MIN',
    'valueOf': 'VALUEOF',
    'compareTo': 'COMPARETO'

}

#Parte realizada por Melina Macias
#Definicion de tokens
tokens = (
    'ENTERO',
    'FLOTANTE',
    'MAS',
    'MULTI',
    'MAYOR',
    'MENOR',
    'LPAREN',
    'RPAREN',
    'RLLAVE',
    'LLLAVE',
    'DOSPUNT',
    'IGUAL',
    'MASIGUAL',
    'DOBLEIGUAL',
    'PUNTO',
    'COMA',
    'ID',
    "CADENA",
) + tuple( reserved.values() )

#ER para tokens definidos
t_MAS = r'\+'
t_MULTI = r'\*'
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_DOSPUNT = r'\:'
t_IGUAL = r'\='
t_MASIGUAL = r'\+='
t_DOBLEIGUAL = r'\={2}'
t_COMA = r'\,'
t_PUNTO = r'\.'
t_CADENA = r'"[a-zA-z0-9\s]*"'

def t_FLOTANTE(t):
    r'(-?[1-9]\d*\.\d+)|0.0'
    t.value = float(t.value)
    return t


def t_ENTERO(t):
    r'(-?[1-9]\d*)|0'
    t.value = int(t.value)
    return t


def t_ID(t):

    r'[A-z_]\w*'
    t.type = reserved.get(t.value, 'ID')

    return t


def t_COMMENT(p):
    r'(^\/\*[\s\w.]*\*\/$)'
    
    pass


def t_error(t):

    errorFormat = ("Error léxico caracter no permitido '{0}' Linea: {1}, columna: {2}"
        .format(t.value[0], t.lineno, t.lexpos))
    
    dumpErrors.append(errorFormat)
    
    t.lexer.skip(1)



def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def getTokens(lexer):

    tokens = []
    
    while True:
    
        tok = lexer.token()
    
        if not tok:
            break

        tokens.append({
        
            "id": tok.type, 
            "colnumber": tok.lexpos, 
            "value": str(tok.value)
        
        })

    return tokens

lexer = lex.lex()
lineTokens = []

import re;

for idx, line in enumerate(sys.argv[1:]):
    
    lexer.input(line)
    lineTokens.append({"tokens": getTokens(lexer)})
    
    if(len(dumpErrors) != 0):
        errorLine = re.sub(
            r'Linea: \d+', "Linea {0}".format(idx + 1), dumpErrors[-1:][0])
        dumpErrors = dumpErrors[:-1]
        dumpErrors.append(errorLine)

if( sys.argv[0] == __file__ ):
    print(json.dumps( {
        "lines": lineTokens,
        "errors": dumpErrors
    }))
