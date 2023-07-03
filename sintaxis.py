import ply.yacc as yacc
from lex import tokens
import lex
precedence = (
    ('left', 'NOT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUAL_EQUAL', 'NOT_EQUAL'),
    ('nonassoc', 'LESS_THAN', 'LESS_THAN_EQUAL', 'GREATER_THAN', 'GREATER_THAN_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULE'),
    #('right', 'UMINUS'),
)
errores=[]

def p_principal (p):
    """
    principal : body 
              | body principal
    """

def p_body (p):
    """body : code_block
            | control_structure
    """

def p_control_structure(p):
    "control_structure : if_statement"

def p_if_statement(p):
    """
    if_statement : IF LPAREN comparison_value RPAREN block_function
                 | IF LPAREN comparison_value RPAREN block_function else_if_statement
                 | IF function comparison value block_function
                 | IF function comparison value block_function else_if_statement
                 | IF LET EQUAL value block_function
                 | IF LET EQUAL value else_if_statement
    """

def p_else_if_statement(p):
    """
    else_if_statement : ELSE block_function
                      | ELSE IF LPAREN comparison_value RPAREN block_function else_if_statement
                      | ELSE IF function comparison value block_function else_if_statement
    """

def p_block_function(p):
    """
    block_function : LBRACE RBRACE 
                   | LBRACE code_block RBRACE 

    """

def p_code_block(p):
    """
    code_block : code_line
               | code_line code_block
    """

def p_code_line(p):
    """
    code_line : code SEMICOLON
    """

def p_code(p):
    """code : function
            | comparison_production
            | value
            | logic_value
            | statement
    """

def p_function (p):
    """function : ID LPAREN RPAREN
                | ID LPAREN value RPAREN
                | ID LPAREN arguments_production RPAREN
                | ID DOT ID LPAREN RPAREN
                | ID DOT ID LPAREN value RPAREN
                | ID DOT ID LPAREN arguments_production RPAREN
    """


def p_statement (p):
    """
    statement : LET ID EQUAL value
              | LET MUT ID EQUAL value
              | CONST ID EQUAL value
              | ID EQUAL ID
              | ID EQUAL aritmetic_operation_production
              | LET ID EQUAL data_structures
              | ID EQUAL data_structures
              | LET MUT ID EQUAL data_structures
    """

def p_data_structures (p):
    "data_structures : tuple"

def p_tuple (p):
    "tuple : LPAREN arguments_production RPAREN"

def p_arguments_production (p):
    """
    arguments_production : value
                         | value COMMA arguments_production
    """


def p_comparison_production (p):
    """
    comparison_production : comparison_value
                          | comparison_value comparison comparison_production
    """

def p_comparison_value (p):
    "comparison_value : value comparison value"

def p_logic_value (p):
    "logic_value : value logic_operator value"

def p_aritmetic_operation_production (p):
    """
    aritmetic_operation_production : aritmetic_operation
                                   | value aritmetic_operator aritmetic_operation
    """

def p_aritmetic_operation (p):
    "aritmetic_operation : value aritmetic_operator value"

def p_aritmetic_operator (p):
    """
    aritmetic_operator : PLUS
                       | MINUS_OPERATOR
                       | TIMES
                       | DIVIDE
                       | MODULE
    """
def p_comparison(p):
    """
    comparison : LESS_THAN
               | GREATER_THAN
               | LESS_THAN_EQUAL
               | GREATER_THAN_EQUAL
               | NOT_EQUAL
               | EQUAL_EQUAL
    """

def p_value(p):
    """
    value : INT
          | FLOAT
          | STRING
          | CHAR
          | BOOL
          | ID
    """

def p_logic_operator(p):
    """
    logic_operator : AND
                   | OR
                   | NOT
    """

def p_error(p):
    syntax_errors = []
    syntax_errors.append("Error de sintaxis en la posición {}: Token inesperado '{}'".format(p.lexpos, p.value))
    # Continuar analizando la entrada
    errores.append("Error de sintaxis en la posición {}: Token inesperado '{}'".format(p.lexpos, p.value))
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