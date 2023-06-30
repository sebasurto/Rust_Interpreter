import ply.yacc as yacc
from lex import tokens

precedence = (
    ('left', 'NOT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUAL_EQUAL', 'NOT_EQUAL'),
    ('nonassoc', 'LESS_THAN', 'LESS_THAN_EQUAL', 'GREATER_THAN', 'GREATER_THAN_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    #('right', 'UMINUS'),
)


#def p_body (p):
   # """body : code
    #        | code body
  #  """
 #   print ("body")
def p_code_block(p):
    """
    code_block : code_line
               | code_line code_block
    """
    print("code_block")

def p_code_line(p):
    """
    code_line : code SEMICOLON
    """
    print("code_line")

def p_code(p):
    """code : function 
            | comparison_production 
            | value 
            | logic_value 
    """
    print("code")

def p_function (p):
    """function : ID LPAREN RPAREN 
                | ID LPAREN value RPAREN
                | ID LPAREN arguments_production RPAREN
    """
    print("function")

def p_arguments_production (p):
    """
    arguments_production : value
                         | value COMMA arguments_production
    """
    print ("arguments_production")


def p_comparison_production (p):
    """
    comparison_production : comparison_value
                          | comparison_value comparison comparison_production
    """
    print ("comparison_production")

def p_comparison_value (p):
    "comparison_value : value comparison value"
    print ("comparison_value")

def p_logic_value (p):
    "logic_value : value logic_operator value"
    print ("logic_value")

def p_comparison(p):
    """
    comparison : LESS_THAN
               | GREATER_THAN
               | LESS_THAN_EQUAL
               | GREATER_THAN_EQUAL
               | NOT_EQUAL
               | EQUAL_EQUAL
    """
    print ("comparison")

def p_value(p):
    """
    value : INT
          | FLOAT
          | STRING
          | CHAR
          | BOOL
          | ID
    """
    print ("value")

def p_logic_operator(p):
    """
    logic_operator : AND
                   | OR
                   | NOT
    """
    print("logic operators")

def p_error(p):
    syntax_errors = []
    syntax_errors.append("Error de sintaxis en la posición {}: Token inesperado '{}'".format(p.lexpos, p.value))
    # Continuar analizando la entrada
    if syntax_errors:
        print("Se encontraron los siguientes errores de sintaxis:")
    for error in syntax_errors:
        print("- " + error)
    else:
        print("Problema en la entrada '{}' ".format(p))
    if p:
        print("Error de sintaxis en token:", p.type)
        # sintactico.errok()
    else:
        print("Syntax error at EOF")

def test_sintaxis (s):
    sintactico = yacc.yacc()
    result = sintactico.parse(s)
    print(result)