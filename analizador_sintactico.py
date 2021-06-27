import ply.yacc as yacc


from main import tokens

def p_algoritmo(p):
    '''algoritmo : declaracion
                   | comparacion
                    | imprimir
                    | agregarElemento
                    | obtenerElemento
                    | crearLista
    '''

def p_declaracion(p):
    '''declaracion :  declaracion_conTipo
                    |
    '''
def p_declaracion_conTipo(p):
    'declaracion_conTipo : tipoVariable ID DOSPUNT tipoDato asignacion '

def p_tipoVariable(p):
    '''tipoVariable : VAR
                    | VAL
    '''

def p_tipoDato(p):
    '''tipoDato :  INTEGER
                   | BOOLEAN
       '''

def p_booleano(p):
    '''booleano :  TRUE
                | FALSE
           '''


def p_asignacion(p):
    ''' asignacion : asignacion_simple
                    |
    '''
def p_asignacion_simple(p):
    'asignacion_simple : IGUAL valor '

def p_valor(p):
    '''valor :    NUMERO
                | ID
                | booleano
    '''

def p_comparacion(p):
    '''comparacion : comparacion_igual
                    | comparacion_mayor
                    |
    '''

def p_comparacion_igual(p):
    'comparacion_igual :  DOBLEIGUAL '

def p_comparacion_mayor(p):
    'comparacion_mayor :  MAYOR '


def p_imprimir(p):
    'imprimir : PRINTLN LPAREN valor RPAREN'

def  p_crearLista(p):
    'crearLista : VAL ID DOSPUNT MUTABLE_LIST MENOR tipoDato MAYOR IGUAL MUTABLE_LIST_OF LPAREN valor RPAREN'



def p_agregarElemento(p):
    'agregarElemento : ID PUNTO ADD LPAREN valor RPAREN'

def p_obtenerElemento(p):
    'obtenerElemento : ID PUNTO GET LPAREN NUMERO RPAREN'


# Build the parser


parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
