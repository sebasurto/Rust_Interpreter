# CODIGO PRELIMINAR PARA EL ANALIZADOR SINTACTICO (NO FUNCIONANDO)
def p_wholeCode(p):
    """
    wholeCode : function_main
    | function_main functions
    | functions
    """

def p_function_main(p):
    """function_main : FN MAIN LPAREN RPAREN LBRACE function_body RBRACE
    | FN MAIN LPAREN RPAREN LBRACE RBRACE
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
    | function_body_line SEMICOLON function_body
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