import ply.yacc as yacc
from lex import tokens
import lex
# Ramon Macias y Sergio Basurto
# Ramón Macías: Reglas semánticas aritméticas, estructura de datos array y estructura de control match
# Sergio Basurto: Reglas semánticas de comparación, estructura de datos tupla y estructura de control if

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
    """
    control_structure : if_statement
                        | match_statement
                        | fn_statement
    """

# Ramon Macias
def p_match_body_line(p):
    """match_body_line : match_cases"""


def p_match_pattern(p):
    """match_pattern : value
    | value PIPE match_pattern"""


def p_match_body(p):
    """match_body : match_body_line
    | match_body_line match_body match_case_default"""


def p_match_statement(p):
    """match_statement : MATCH ID LBRACE match_body RBRACE"""


def p_match_cases(p):
    """match_cases : match_case
    | match_case match_cases """


def p_match_case(p):
    """match_case : match_pattern FAT_ARROW block_function"""


def p_match_case_default(p):
    """match_case_default : UNDERSCORE FAT_ARROW block_function"""
    
def p_if_statement(p):
    """
    if_statement : IF LPAREN comparison_value RPAREN block_function
                 | IF LPAREN comparison_value RPAREN block_function else_if_statement
                 | IF function comparison value block_function
                 | IF function comparison value block_function else_if_statement
                 | IF LET EQUAL value block_function
                 | IF LET EQUAL value else_if_statement
    """
def p_fn_statement (p):
    """
    fn_statement : FN MAIN LPAREN RPAREN block_function
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

def p_print (p):
    """
    print : PRINT LPAREN value RPAREN
          | PRINT LPAREN STRING DOT ID RPAREN 
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
    """
    data_structures : tuple
                    | array
    """


def p_array_i32(p):
    "array : LBRACKET array_elements RBRACKET"

def p_array_elements_i32(p):
    """array_elements : INT
    | array_elements COMMA INT"""

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
    if p[2] == "<":
        p[0] = p[1] < p[3]
    elif p[2] == ">":
        p[0] = p[1] > p[3]
    elif p[2] == "<=":
        p[0] = p[1] <= p[3]
    elif p[2] == ">=":
        p[0] = p[1] >= p[3]
    elif p[2] == "!=":
        p[0] = p[1] != p[3]
    elif p[2] == "==":
        p[0] = p[1] == p[3]

def p_logic_value (p):
    "logic_value : value logic_operator value"
    if p[2] == "&&":
        p[0] = p[1] and p[3]
    elif p[2] == "||":
        p[0] = p[1] or p[3]
    elif p[2] == "!":
        p[0] = not p[1]

def p_aritmetic_operation_production (p):
    """
    aritmetic_operation_production : aritmetic_operation
                                   | value aritmetic_operator aritmetic_operation
    """
    p[0] = 0
    if len(p) == 2:
        p[0] = p[1]
    else:
        operations = len(p)//2
        for i in range(1, operations+1):
            if p[2*i-1] == "+":
                p[0] += p[2*i]
            elif p[2*i-1] == "-":
                p[0] -= p[2*i]
            elif p[2*i-1] == "*":
                p[0] *= p[2*i]
            elif p[2*i-1] == "/":
                p[0] /= p[2*i]
            elif p[2*i-1] == "%":
                p[0] %= p[2*i]



def p_aritmetic_operation (p):
    "aritmetic_operation : value aritmetic_operator value"
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]
    elif p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]
    elif p[2] == "%":
        p[0] = p[1] % p[3]

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
          | array
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