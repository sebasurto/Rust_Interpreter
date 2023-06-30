import interface as fc
import ply.yacc as yacc
import lex as lxc
from lex import tokens
import sintaxis as sntx

fc.create_interface ()
# lex.test_Sergio_Basurto()
# lex.test_Ramon_Macias()

# Build the parser
def p_sentence(p):
    """sentence : let_statement"""


# Ramon Macias

def p_match_body_line(p):
    """match_body_line : match_cases"""


def p_match_pattern(p):
    """match_pattern : value
    | value PIPE match_pattern"""


def p_match_body(p):
    """match_body : match_body_line
    | match_body_line match_body"""


def p_edc_match(p):
    """edc_match : MATCH ID LBRACE match_body RBRACE"""


def p_match_cases(p):
    """match_cases : match_case
    | match_case match_cases"""


def p_match_case(p):
    """match_case : match_pattern FAT_ARROW LBRACE code_body RBRACE"""


def p_match_case_default(p):
    """match_case : DEFAULT_MATCH FAT_ARROW LBRACE code_body RBRACE"""


def p_code_body(p):
    """code_body : code_body_line 
    | code_body_line code_body"""


def p_code_body_line(p):
    """code_body_line : expression SEMICOLON
    | statement SEMICOLON
    | SEMICOLON"""


def p_expression(p):
    """expression : value
    | expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | expression MODULO expression
    | expression EQUAL_EQUAL expression
    | expression NOT_EQUAL expression
    | expression GREATER_THAN expression
    | expression GREATER_THAN_EQUAL expression
    | expression LESS_THAN expression
    | expression LESS_THAN_EQUAL expression
    | expression PIPE_PIPE expression
    | expression AMPERSAND_AMPERSAND expression
    | expression PIPE expression
    | expression AMPERSAND expression
    | expression BANG expression
    | expression EQUAL expression
    | expression DOT ID
    | expression LBRACKET expression RBRACKET
    | expression LBRACE expression RBRACE
    | expression COLON expression
    | expression DOUBLE_COLON expression
    | expression ARROW expression
    | expression FAT_ARROW expression
    | expression COMMA expression
    | expression SEMICOLON expression
    | expression AT expression
    | expression UNDERSCORE expression
    | expression DOUBLE_QUOTE expression
    | expression CHAR expression"""

def p_expression_function_call(p):
    """expression : ID LPAREN RPAREN
    | ID LPAREN parameters RPAREN"""


def p_let_array_i32(p):
    """array : LET ID EQUAL LBRACKET array_elements RBRACKET"""

def p_array_elements_i32(p):
    """array_elements : INT
    | array_elements COMMA INT"""




def p_statement(p):
    """statement : let_statement
    | let_mut_statement
    | const_statement
    | if_statement
    | while_statement
    | for_statement
    | match_statement
    | function_statement
    | return_statement
    | break_statement
    | continue_statement"""


def p_let_statement(p):
    """let_statement : LET ID EQUAL expression"""


def p_let_mut_statement(p):
    """let_mut_statement : LET MUT ID EQUAL expression"""


def p_const_statement(p):
    """const_statement : CONST ID EQUAL expression"""


# TODO: Missing correct and complete implementation
def p_if_statement(p):
    """if_statement : IF expression LBRACE code_body RBRACE"""


# TODO: Missing correct and complete implementation
def p_while_statement(p):
    """while_statement : WHILE expression LBRACE code_body RBRACE"""


# TODO: Missing correct and complete implementation
def p_for_statement(p):
    """for_statement : FOR ID IN expression LBRACE code_body RBRACE"""


def p_match_statement(p):
    """match_statement : edc_match"""


def p_function_statement(p):
    """function_statement : function
    | function_main"""


def p_function_main(p):
    "function_main : FN MAIN LPAREN RPAREN LBRACE code_body RBRACE"


def p_function(p):
    """function : FN ID LPAREN RPAREN LBRACE code_body RBRACE
    | FN ID LPAREN parameters RPAREN LBRACE code_body RBRACE
    | FN ID LPAREN parameters RPAREN ARROW ID LBRACE code_body RBRACE"""


def p_parameters(p):
    """parameters : ID
    | ID COMMA parameters"""


def p_return_statement(p):
    "return_statement : RETURN expression SEMICOLON"


def p_break_statement(p):
    "break_statement : BREAK SEMICOLON"


def p_continue_statement(p):
    "continue_statement : CONTINUE SEMICOLON"

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
#Sergio Basurto estructura IF
def p_comparison(p):
    """
    comparison : EQUAL_EQUAL
    | LESS_THAN
    | GREATER_THAN
    | LESS_THAN_EQUAL
    | GREATER_THAN_EQUAL
    | NOT_EQUAL
    """
def p_comparison_parameter (p):
    """
    comparison_parameter : value comparison value
    """
def p_if_statement(p):
    """
    if_statement : IF LPAREN comparison_parameter RPAREN block
                 | IF LPAREN comparison_parameter RPAREN block else_if_statement
    """

def p_else_if_statement(p):
    """
    else_if_statement : ELSE if_statement
                      | ELSE IF LPAREN comparison_parameter RPAREN block else_if_statement
    """
def p_block(p):
    """
    block : LBRACE statements RBRACE
          | LBRACE RBRACE
    """
def p_statements(p):
    """
    statements : statement
               | statement statements
    """
def p_error(p):
    if p:
        print("Error de sintaxis en token:", p.type)
        # sintactico.errok()
    else:
        print("Syntax error at EOF")

s = '''
5 < 6
            8 > 10
            7 <= 9
            8 >= 9
            let i = 5.
            let f = 56
            let mut n = -7.
            let n = -7.5
            fn main() {
                // Variables
                let mut counter = 0;
                let my_string = String::from("Hola, mundo!");
                let my_float = 3.14;

                // While loop
                while counter < 5 {
                    println!("Contador: {}", counter);
                    counter += 1;
                }

                // For loop
                for i in 0..5 {
                    println!("Valor de i: {}", i);
                }

                // If statement
                if my_string.len() > 10 {
                    println!("La cadena es larga");
                } else {
                    println!("La cadena es corta");
                }

                // Mostrar valores
                println!("Cadena: {}", my_string);
                println!("Flotante: {}", my_float);
            }
'''
n = """
    max ();
    5 > 6;
    println ( "hola mundo" );
    1 >= 3;
    1 == 2;
    2 > 4;
    print (4 );
    printarg (4,5); 
    5.6;
    hola;
    7;
    true;
    false;
    True;
    TRUE;
    False;
    FALSE;
    "hola mundo";
    'h';
    true || false;
    hola();
    5 < 6;
    8 > 10;
    7 <= 9;
    8 >= 9;
    6 == 8;
    6 != 6;
    if my_string.len() > 10 {
                    println!("La cadena es larga");
                } else {
                    println!("La cadena es corta");
                }
    """
    
lxc.test_lex(n)
sntx.test_sintaxis(n)