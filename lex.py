import ply.lex as lex

reserved = {'while': 'WHILE'
}

 #Sequencia de tokens, puede ser lista o tupla
tokens = (
    'COMMENS',
    'EQUALSC',
    'EQUALS',
    'FLOAT',
    'INT',
    #'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
  'ID',
) + tuple(reserved.values())
 
 #Exp Regulares para tokens de símbolos
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
#t_NUMBER = r'\d+'
t_INT = r'\d+'
t_FLOAT = r'-?\d*\.\d+'
t_EQUALS = '='
t_EQUALSC = '=='
 
 #Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_ID(t):
  r'[a-zA-Z_]\w+'
  t.type = reserved.get(t.value,'ID')
  return t

 
 # Ignorar lo que no sea un token en mi LP
t_ignore  = ' \t'
 
 #Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)
 
 #Contruir analizador

def _COMMENS(t):
  r'\#.*'
  pass