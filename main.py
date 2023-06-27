import interface as fc
import ply.yacc as yacc
from lex import tokens
import lex


# fc.create_interface ()
# lex.test_Sergio_Basurto()
# lex.test_Ramon_Macias()

# Build the parser
def p_wholeCode(p):
    """
    wholeCode : function_main
    | function_main functions
    | functions
    """

def p_function_main(p):
    """function_main : FN MAIN LPAREN RPAREN LBRACE function_body RBRACE
    | FN MAIN LPAREN RPAREN LBRACE RBRACE
    | FN MAIN LPAREN parameters RPAREN LBRACE function_body RBRACE
    | FN MAIN LPAREN parameters RPAREN LBRACE RBRACE
    """

def p_functions(p):
    """
    functions : function
    | function functions
    """


def p_function(p):
    """
    function : FN ID LPAREN RPAREN LBRACE function_body RBRACE
    | FN ID LPAREN RPAREN LBRACE RBRACE
    | FN ID LPAREN parameters RPAREN LBRACE function_body RBRACE
    | FN ID LPAREN parameters RPAREN LBRACE RBRACE
    | FN ID LPAREN parameters RPAREN ARROW ID LBRACE function_body RBRACE
    """

def p_parameters(p):
    """
    parameters : ID
    | ID COMMA parameters
    """

def p_function_body(p):
    """
    function_body : function_body_line
    | function_body_line function_body
    """

def p_function_body_line(p):
    """function_body_line : expression SEMICOLON
    | statement"""

def p_statement(p):
    """
    statement : assignation
    | expression SEMICOLON
    | SEMICOLON
    """

def p_expression(p):
    """
    expression : assignation
    | value SEMICOLON
    """

def p_assignation(p):
    """assignation : LET ID EQUAL value SEMICOLON
    | LET ID EQUAL value"""

def p_value(p):
    """value : INT
    | FLOAT
    | STRING
    | CHAR
    | BOOL
    | ID
    """
#Sergio Basurto 26/06/2023 tuple structure
def p_tuple(p):
    """
    tuple : LPAREN tuple_elements RPAREN
    """
#Sergio Basurto 26/06/2023 
def p_tuple_elements(p):
    """
    tuple_elements : value
                   | value COMMA tuple_elements
    """

def p_error(p):
    if p:
        print("Error de sintaxis en token:", p.type)
        # sintactico.errok()
    else:
        print("Syntax error at EOF")


sintactico = yacc.yacc()

while True:
    try:
        s = input('rust > ')
    except EOFError:
        break
    if not s: continue
    result = sintactico.parse(s)
    if result is not None:
        print(result)
