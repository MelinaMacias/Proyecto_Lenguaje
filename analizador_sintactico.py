
import ply.yacc as yacc

from main import tokens

def p_sentencias(p):
    '''sentencias : declaracion
					| asignacion
					| expresion
					| estructuras_control
                    | imprimir
					| obtenerEntrada
					| operacionesBasicas
					| operacionesEstructuras
					| declaracionFunciones
					| funcionesTipoDato
					| casting

    '''


def p_expresion(p):
	'''expresion : comparacion
					| LPAREN expresion RPAREN
	'''


def p_estructuras_control(p):
	'''estructuras_control : ifSimple
							| ifElse
							| while
	'''


def p_casting(p):
	'''casting :  numeroOrId CASTOPERATOR INTEGER
				| flotanteOrId CASTOPERATOR FLOAT
				| numeroOrId CASTOPERATOR FLOAT
				| flotanteOrId CASTOPERATOR STRING
				| CADENA CASTOPERATOR FLOAT
				| CADENA CASTOPERATOR INTEGER
				| numeroOrId CASTOPERATOR STRING
	'''


def p_operacionesBasicas(p):
	'''operacionesBasicas : operacionesNumeros'''


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
	'declaracionFunciones : FUN ID LPAREN secuenciaParametros RPAREN LLLAVE sentenciasAnidadas RLLAVE'


def p_ifSimple(p):
	'ifSimple : IF LPAREN expresion RPAREN LLLAVE sentenciasAnidadas RLLAVE'


def p_ifElse(p):
	'''ifElse : ifSimple ELSE LLLAVE sentenciasAnidadas RLLAVE
				| ifSimple ELSE ifSimple'''


def p_sentenciasAnidadas(p):
	'''sentenciasAnidadas : sentencias 
						| sentencias sentenciasAnidadas
	'''

def p_while(p):
	'while : WHILE LPAREN expresion RPAREN LLLAVE sentenciasAnidadas RLLAVE'


def p_secuenciaNumerosOrId(p):
	'''secuenciaNumerosOrId : numeroOrId
						| numeroOrId COMA secuenciaNumerosOrId
	'''


def p_secuenciaBooleanosOrId(p):
	'''secuenciaBooleanosOrId : booleanoOrId
					| booleanoOrId COMA secuenciaBooleanosOrId
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


#Elaborado por Melina Macías-Regla semantica
#Declaracion de variables sujetas al tipo de dato

def p_declaracion_conTipo(p):
    '''declaracion_conTipo : tipoIdentificador ID DOSPUNT INTEGER IGUAL numeroOrId
							| tipoIdentificador ID DOSPUNT INTEGER IGUAL operacionesNumeros
							| tipoIdentificador ID DOSPUNT BOOLEAN IGUAL booleanoOrId
						'''

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
							| IGUAL obtenerEntrada
							| IGUAL obtenerElementoLista
							| IGUAL casting
	'''


def p_asignacion_suma(p):
    '''asignacion_suma : MASIGUAL numeroOrId
    					| MASIGUAL FLOTANTE
						| MASIGUAL operacionesBasicas
						| MASIGUAL casting
	'''


# Reglas semanticas para las operaciones de suma y multiplicacion
# * Solo permitidas con números o variables
###################################################################

def p_operacionesNumeros(p):
	'''operacionesNumeros : numeroOrId operacionIntermedia
							| flotanteOrId operacionIntermedia
	'''


def p_operacionIntermedia(p):
	'''operacionIntermedia : operadorNumeros numeroOrId
							| operadorNumeros flotanteOrId
							| operadorNumeros numeroOrId operacionIntermedia
							| operadorNumeros flotanteOrId operacionIntermedia
	'''

def p_operadorNumeros(p):
	'''operadorNumeros : MAS 
						| MULTI
	'''

def p_valor(p):
    '''valor :    ENTERO
    			| FLOTANTE
				| CADENA
                | ID
                | booleano
    '''

def p_comparacion(p):
    '''comparacion : comparacion_igualdad
                    | comparacion_menorque
    '''



# Reglas semanticas de comparacion
###################################################################
def p_comparacion_igualdad(p):
    '''comparacion_igualdad : numeroOrId DOBLEIGUAL numeroOrId
							| ID DOBLEIGUAL numeroOrId
							| flotanteOrId DOBLEIGUAL flotanteOrId
							| ID DOBLEIGUAL flotanteOrId
							| booleanoOrId DOBLEIGUAL booleanoOrId
							| ID DOBLEIGUAL booleanoOrId
							| expresion DOBLEIGUAL expresion
	'''


def p_comparacion_menorque(p):
    '''comparacion_menorque : numeroOrId MENOR numeroOrId
							| ID MENOR numeroOrId
							| flotanteOrId MENOR flotanteOrId
							| ID MENOR flotanteOrId
							| booleanoOrId MENOR booleanoOrId
							| ID MENOR booleanoOrId
							| expresion MENOR expresion
	'''


def p_obtenerEntrada(p):
	'obtenerEntrada : READ_LINE LPAREN RPAREN'


def p_imprimir(p):
    '''imprimir : PRINTLN LPAREN valor RPAREN
				| PRINTLN LPAREN obtenerElementoLista RPAREN
	'''


#Elaborador por Melina Macias - Regla semantica
#Creacion de estructuras de datos acorde al tipo de dato

def  p_crearLista(p):
    '''crearLista : tipoIdentificador ID DOSPUNT MUTABLE_LIST MENOR INTEGER MAYOR IGUAL MUTABLE_LIST_OF LPAREN secuenciaNumerosOrId RPAREN
    				| tipoIdentificador ID DOSPUNT MUTABLE_LIST MENOR BOOLEAN MAYOR IGUAL MUTABLE_LIST_OF LPAREN secuenciaBooleanosOrId RPAREN
    				'''


def  p_crearConjunto(p):
    '''crearConjunto : tipoIdentificador ID DOSPUNT MUTABLE_SET MENOR INTEGER MAYOR IGUAL MUTABLE_SET_OF LPAREN secuenciaNumerosOrId RPAREN
    				| 	tipoIdentificador ID DOSPUNT MUTABLE_SET MENOR BOOLEAN MAYOR IGUAL MUTABLE_SET_OF LPAREN secuenciaBooleanosOrId RPAREN
    					'''


def p_agregarElementoLista(p):
    'agregarElementoLista : ID PUNTO ADD LPAREN valor RPAREN'


def p_obtenerElementoLista(p):
    'obtenerElementoLista : ID PUNTO GET LPAREN numeroOrId RPAREN'


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


def p_convertirABoolean(p):
	'convertirABoolean : BOOLEAN PUNTO VALUEOF LPAREN valor RPAREN'


def p_comparacionBooleanos(p):
	'comparacionBooleanos : BOOLEAN PUNTO COMPARETO LPAREN booleanoOrId RPAREN'


def p_numeroOrId(p):
	'''numeroOrId : ENTERO
					| ID
	'''


def p_flotanteOrId(p):
	'''flotanteOrId : FLOTANTE
						| ID
	'''


def p_booleanoOrId(p):
	'''booleanoOrId : booleano
					| ID
	'''

def p_error(p):

	errorFormat = ("Error sintáctico sentencia errónea Linea: {0}, columna: {1}"
		.format(p.lineno, p.lexpos) )

	print(errorFormat)


# Build the parser

parser = yacc.yacc()

# Algoritmo de prueba 
###################################################################
algoritmo = '''

var listaCodigos:MutableList<Integer> = mutableListOf(1111, 1204, 2223, 4245);
var numeroCodigo:Integer = 0;
var entrada = readLine();

numeroCodigo = (Integer) entrada;

if( codigo < 4) { 
	
	var contador:Integer = 0
	while( contador < 4 ) { 
		
		println( listaCodigos.get(contador) )
		contador += 1
	
	}

}

'''.split(";")

for x in range( len(algoritmo) ):

	result = parser.parse(algoritmo[x])
	print(result)
