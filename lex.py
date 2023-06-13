import ply.lex as lex

reserved = {'while': 'WHILE', 'where':'WHERE','use':'USE','unsafe':'UNSAFE', 'union':'UNION','type':'TYPE',
            'true':'TRUE','trair':'TRAIT','super':'SUPER','struct':'STRUCT','static':'STATIC','self':'SELF',
            'Self':'sELF','return':'RETURN','ref':'REF','pub':'PUB','mut':'MUT','move':'MOVE','mod':'MOD','match':'MATCH',
            'loop':'LOOP','let':'LET','in':'IN','impl':'IMPL', 'if':'IF','for':'FOR','fn':'FN','false':'FALSE',
            'extern':'EXTERN','enum':'ENUM', 'else':'ELSE', 'dyn':'DYN','crate':'CRATE', 'continue':'CONTINUE',
            'const':'CONST', 'break': 'BREAK', 'await':'AWAIT', 'async':'ASYNC', 'as':'AS'
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
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_THAN_EQUAL',
    'GREATER_THAN_EQUAL',
    'CHAR',
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
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUAL = r'<='
t_GREATER_THAN_EQUAL = r'>='
t_CHAR = r'\'[a-zA-Z]\''
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
  r'//.*'
  pass

def test_Sergio_Basurto():
  lexer = lex.lex()
  data = ''' 5 < 6
            8 > 10
            7 <= 9
            8 >= 9
            let c = 'Z'
            //comentario

        '''
  lexer.input (data)
  while True:
    tok = lexer.token()
    if not tok: 
      break      #Rompe
    print(tok)