
import ply.yacc as yacc


from main import tokens

def p_sentencias(p):
    '''sentencias : declaracion
					| expresion
					| estructuras_control
                    | imprimir
					| operacionesEstructuras
					| declaracionFunciones
					| funcionesTipoDato


    '''


def p_expresion(p):
	'''expresion : asignacion
					| comparacion
					| operacionesBasicas
	'''


def p_estructuras_control(p):
	'''estructuras_control : ifSimple
							| ifElse
							| while
	'''


def p_operacionesBasicas(p):
	'''operacionesBasicas : sumaValores
							| multValores
	'''


def p_funcionesTipoDato(p):
	'''funcionesTipoDato : encontrarMayor
			| encontrarMenor
			| convertirABoolean
			| comparacionBooleanos
	'''


def p_operacionesEstructuras(p):
	'''operacionesEstructuras : agregarElementoLista
                    			| obtenerElementoLista
                    			| obtenerIteradorConjunto
                    			| borrarElementosConjunto
	'''


def p_declaracionFunciones(p):
	'declaracionFunciones : FUN ID LPAREN secuenciaParametros RPAREN LLLAVE sentencias RLLAVE'


def p_ifSimple(p):
	'ifSimple : IF LPAREN expresion RPAREN LLLAVE sentencias RLLAVE'


def p_ifElse(p):
	'''ifElse : ifSimple ELSE LLLAVE sentencias RLLAVE
				| ifSimple ELSE ifSimple'''


def p_while(p):
	'while : WHILE LPAREN expresion RPAREN LLLAVE sentencias RLLAVE'


def p_secuenciaNumeros(p):
	'''secuenciaNumeros : NUMERO
						| NUMERO COMA secuenciaNumeros
	'''


def p_secuenciaBooleanos(p):
	'''secuenciaBooleanos : booleano
					| booleano COMA secuenciaBooleanos
	'''


def p_secuenciaIdentificadores(p):
	'''secuenciaIdentificadores : ID
					| ID COMA secuenciaIdentificadores
	'''


def p_secuencia(p):
	'''secuencia : secuenciaNumeros
				| secuenciaBooleanos
				| secuenciaIdentificadores
	'''


def p_secuenciaParametros(p):
	'''secuenciaParametros : ID DOSPUNT tipoDato
							| ID DOSPUNT tipoDato COMA secuenciaParametros

	'''


def p_asignacion(p):
	'''asignacion : ID asignacion_simple
					| ID asignacion_suma
	'''

def p_declaracion(p):
    '''declaracion :  declaracion_conTipo
                    | declaracion_sinTipo
                    | crearLista
					| crearConjunto
    '''


def p_declaracion_conTipo(p):
    'declaracion_conTipo : tipoIdentificador ID DOSPUNT tipoDato asignacion_declaracion'


def p_declaracion_sinTipo(p):
    'declaracion_sinTipo : tipoIdentificador ID asignacion_declaracion'	


def p_tipoIdentificador(p):
    '''tipoIdentificador : VAR
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


def p_asignacion_declaracion(p):
    ' asignacion_declaracion : asignacion_simple'


def p_asignacion_simple(p):
    '''asignacion_simple : IGUAL valor
							| IGUAL operacionesBasicas
	'''


def p_asignacion_suma(p):
    '''asignacion_suma : MASIGUAL valor
						| MASIGUAL operacionesBasicas
	'''

def p_sumaValores(p):
	'sumaValores : valor MAS valor'


def p_multValores(p):
	'multValores : valor MULTI valor'


def p_valor(p):
    '''valor :    NUMERO
                | ID
                | booleano
    '''


def p_comparacion(p):
    '''comparacion : comparacion_igualdad
                    | comparacion_menorque
    '''


def p_comparacion_igualdad(p):
    '''comparacion_igualdad : valor DOBLEIGUAL valor
	'''


def p_comparacion_menorque(p):
    '''comparacion_menorque : valor MENOR valor
	'''


def p_imprimir(p):
    'imprimir : PRINTLN LPAREN valor RPAREN'


def  p_crearLista(p):
    'crearLista : tipoIdentificador ID DOSPUNT MUTABLE_LIST MENOR tipoDato MAYOR IGUAL MUTABLE_LIST_OF LPAREN secuencia RPAREN'


def  p_crearConjunto(p):
    'crearConjunto : tipoIdentificador ID DOSPUNT MUTABLE_SET MENOR tipoDato MAYOR IGUAL MUTABLE_SET_OF LPAREN secuencia RPAREN'


def p_agregarElementoLista(p):
    'agregarElementoLista : ID PUNTO ADD LPAREN valor RPAREN'


def p_obtenerElementoLista(p):
    'obtenerElementoLista : ID PUNTO GET LPAREN NUMERO RPAREN'


def p_obtenerIteradorConjunto(p):
	'obtenerIteradorConjunto : ID PUNTO GET_ITERATOR LPAREN RPAREN'


def p_borrarElementosConjunto(p):
	'borrarElementosConjunto : ID PUNTO CLEAR_ALL LPAREN RPAREN'

#Elaborado por Melina Macias -
#Validación semantica para los argumentos de las funciones que trabajan con tipos de datos.

def p_encontrarMayor(p):
	'encontrarMayor : INTEGER PUNTO MAX LPAREN numeroOrId COMA numeroOrId RPAREN'


def p_encontrarMenor(p):
	'encontrarMenor : INTEGER PUNTO MIN LPAREN numeroOrId COMA numeroOrId RPAREN'


def p_numeroOrId(p):
	'''numeroOrId : NUMERO
					| ID
	'''


def p_convertirABoolean(p):
	'convertirABoolean : BOOLEAN PUNTO VALUEOF LPAREN valor RPAREN'


def p_comparacionBooleanos(p):
	'comparacionBooleanos : BOOLEAN PUNTO COMPARETO LPAREN booleanoOrId RPAREN'


def p_booleanoOrId(p):
	'''booleanoOrId : booleano
					| ID
	'''



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
