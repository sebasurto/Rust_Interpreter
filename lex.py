import ply.lex as lex
#Ramon Macias y Sergio Basurto
reserved = {
    'while': 'WHILE',
    'where': 'WHERE',
    'use': 'USE',
    'unsafe': 'UNSAFE',
    'union': 'UNION',
    'type': 'TYPE',
    'true': 'TRUE',
    'trair': 'TRAIT',
    'super': 'SUPER',
    'struct': 'STRUCT',
    'static': 'STATIC',
    'self': 'SELF',
    'Self': 'SELF',
    'return': 'RETURN',
    'ref': 'REF',
    'pub': 'PUB',
    'mut': 'MUT',
    'move': 'MOVE',
    'mod': 'MOD',
    'match': 'MATCH',
    'loop': 'LOOP',
    'let': 'LET',
    'in': 'IN',
    'impl': 'IMPL',
    'if': 'IF',
    'for': 'FOR',
    'fn': 'FN',
    'false': 'FALSE',
    'extern': 'EXTERN',
    'enum': 'ENUM',
    'else': 'ELSE',
    'dyn': 'DYN',
    'crate': 'CRATE',
    'continue': 'CONTINUE',
    'const': 'CONST',
    'break': 'BREAK',
    'await': 'AWAIT',
    'async': 'ASYNC',
    'as': 'AS'
}


# Sequencia de tokens, puede ser lista o tupla
# Ramon Macias y Sergio Basurto (Ambos trabajamos en esta parte)
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'COLON',
    'DOUBLE_COLON',
    'ARROW',
    'FAT_ARROW',
    'PIPE',
    'PIPE_PIPE',
    'AMPERSAND',
    'AMPERSAND_AMPERSAND',
    'BANG',
    'EQUAL',
    'EQUAL_EQUAL',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_THAN_EQUAL',
    'GREATER_THAN_EQUAL',
    'NOT_EQUAL',
    'MODULO',
    'UNDERSCORE',
    'AT',
) + tuple(reserved.values())

# Expresiones regulares para los tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_DOUBLE_COLON = r'::'
t_ARROW = r'->'
t_FAT_ARROW = r'=>'
t_PIPE = r'\|'
t_PIPE_PIPE = r'\|\|'
t_AMPERSAND = r'&'
t_AMPERSAND_AMPERSAND = r'&&'
t_BANG = r'!'
t_EQUAL = r'='
t_EQUAL_EQUAL = r'=='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUAL = r'<='
t_GREATER_THAN_EQUAL = r'>='
t_NOT_EQUAL = r'!='
t_MODULO = r'%'
t_UNDERSCORE = r'_'
t_AT = r'@'


# Para contabilizar nro de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

 # Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'

# Presentación de errores léxicos


def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

 # Contruir analizador


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
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # Rompe
        print(tok)


def test_Ramon_Macias():
    lexer = lex.lex()
    data = ''' 2==1
            2!=1
            2<1
            2>1
            2<=1
            2>=1
            let x=51
            // let x=1
            y!=z
            '''
    lexer.input(data)
    while tok := lexer.token():
        print(tok)
