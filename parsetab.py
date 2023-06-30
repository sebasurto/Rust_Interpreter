
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftNOTleftORleftANDnonassocEQUAL_EQUALNOT_EQUALnonassocLESS_THANLESS_THAN_EQUALGREATER_THANGREATER_THAN_EQUALleftPLUSMINUSleftTIMESDIVIDEMODULOAMPERSAND AND ARROW AS ASYNC AT AWAIT BOOL BREAK CASE CHAR COLON COMMA COMMENS CONST CONTINUE CRATE DIVIDE DOT DOUBLE_COLON DOUBLE_QUOTE DYN ELSE ENUM EQUAL EQUAL_EQUAL EXTERN FAT_ARROW FLOAT FN FOR GREATER_THAN GREATER_THAN_EQUAL ID IF IMPL IN INT LBRACE LBRACKET LESS_THAN LESS_THAN_EQUAL LET LOOP LPAREN MAIN MATCH MINUS MOD MODULO MOVE MUT NAME_FUNCTION NOT NOT_EQUAL OR PIPE PLUS PUB RBRACE RBRACKET REF RETURN RPAREN SELF SEMICOLON STATIC STRING STRUCT SUPER TIMES TRAIT TYPE UNDERSCORE UNION UNSAFE USE WHERE WHILE sELF\n    code_block : code_line\n               | code_line code_block\n    \n    code_line : code SEMICOLON\n    code : function \n            | comparison_production \n            | value \n            | logic_value \n    function : ID LPAREN RPAREN \n                | ID LPAREN value RPAREN\n                | ID LPAREN arguments_production RPAREN\n    \n    arguments_production : value\n                         | value COMMA arguments_production\n    \n    comparison_production : comparison_value\n                          | comparison_value comparison comparison_production\n    comparison_value : value comparison valuelogic_value : value logic_operator value\n    comparison : LESS_THAN\n               | GREATER_THAN\n               | LESS_THAN_EQUAL\n               | GREATER_THAN_EQUAL\n               | NOT_EQUAL\n               | EQUAL_EQUAL\n    \n    value : INT\n          | FLOAT\n          | STRING\n          | CHAR\n          | BOOL\n          | ID\n    \n    logic_operator : AND\n                   | OR\n                   | NOT\n    '
    
_lr_action_items = {'ID':([0,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,39,],[8,8,-3,31,31,-29,-30,-31,-17,-18,-19,-20,-21,-22,31,31,31,]),'INT':([0,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,39,],[10,10,-3,10,10,-29,-30,-31,-17,-18,-19,-20,-21,-22,10,10,10,]),'FLOAT':([0,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,39,],[11,11,-3,11,11,-29,-30,-31,-17,-18,-19,-20,-21,-22,11,11,11,]),'STRING':([0,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,39,],[12,12,-3,12,12,-29,-30,-31,-17,-18,-19,-20,-21,-22,12,12,12,]),'CHAR':([0,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,39,],[13,13,-3,13,13,-29,-30,-31,-17,-18,-19,-20,-21,-22,13,13,13,]),'BOOL':([0,2,16,17,18,19,20,21,22,23,24,25,26,27,28,29,39,],[14,14,-3,14,14,-29,-30,-31,-17,-18,-19,-20,-21,-22,14,14,14,]),'$end':([1,2,15,16,],[0,-1,-2,-3,]),'SEMICOLON':([3,4,5,6,7,8,9,10,11,12,13,14,30,31,32,33,36,38,40,],[16,-4,-5,-6,-7,-28,-13,-23,-24,-25,-26,-27,-16,-28,-15,-8,-14,-9,-10,]),'AND':([6,8,10,11,12,13,14,],[19,-28,-23,-24,-25,-26,-27,]),'OR':([6,8,10,11,12,13,14,],[20,-28,-23,-24,-25,-26,-27,]),'NOT':([6,8,10,11,12,13,14,],[21,-28,-23,-24,-25,-26,-27,]),'LESS_THAN':([6,8,9,10,11,12,13,14,31,32,37,],[22,-28,22,-23,-24,-25,-26,-27,-28,-15,22,]),'GREATER_THAN':([6,8,9,10,11,12,13,14,31,32,37,],[23,-28,23,-23,-24,-25,-26,-27,-28,-15,23,]),'LESS_THAN_EQUAL':([6,8,9,10,11,12,13,14,31,32,37,],[24,-28,24,-23,-24,-25,-26,-27,-28,-15,24,]),'GREATER_THAN_EQUAL':([6,8,9,10,11,12,13,14,31,32,37,],[25,-28,25,-23,-24,-25,-26,-27,-28,-15,25,]),'NOT_EQUAL':([6,8,9,10,11,12,13,14,31,32,37,],[26,-28,26,-23,-24,-25,-26,-27,-28,-15,26,]),'EQUAL_EQUAL':([6,8,9,10,11,12,13,14,31,32,37,],[27,-28,27,-23,-24,-25,-26,-27,-28,-15,27,]),'LPAREN':([8,],[28,]),'RPAREN':([10,11,12,13,14,28,31,34,35,41,42,],[-23,-24,-25,-26,-27,33,-28,38,40,-11,-12,]),'COMMA':([10,11,12,13,14,31,34,41,],[-23,-24,-25,-26,-27,-28,39,39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code_block':([0,2,],[1,15,]),'code_line':([0,2,],[2,2,]),'code':([0,2,],[3,3,]),'function':([0,2,],[4,4,]),'comparison_production':([0,2,29,],[5,5,36,]),'value':([0,2,17,18,28,29,39,],[6,6,30,32,34,37,41,]),'logic_value':([0,2,],[7,7,]),'comparison_value':([0,2,29,],[9,9,9,]),'logic_operator':([6,],[17,]),'comparison':([6,9,37,],[18,29,18,]),'arguments_production':([28,39,],[35,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code_block","S'",1,None,None,None),
  ('code_block -> code_line','code_block',1,'p_code_block','sintaxis.py',23),
  ('code_block -> code_line code_block','code_block',2,'p_code_block','sintaxis.py',24),
  ('code_line -> code SEMICOLON','code_line',2,'p_code_line','sintaxis.py',30),
  ('code -> function','code',1,'p_code','sintaxis.py',35),
  ('code -> comparison_production','code',1,'p_code','sintaxis.py',36),
  ('code -> value','code',1,'p_code','sintaxis.py',37),
  ('code -> logic_value','code',1,'p_code','sintaxis.py',38),
  ('function -> ID LPAREN RPAREN','function',3,'p_function','sintaxis.py',43),
  ('function -> ID LPAREN value RPAREN','function',4,'p_function','sintaxis.py',44),
  ('function -> ID LPAREN arguments_production RPAREN','function',4,'p_function','sintaxis.py',45),
  ('arguments_production -> value','arguments_production',1,'p_arguments_production','sintaxis.py',51),
  ('arguments_production -> value COMMA arguments_production','arguments_production',3,'p_arguments_production','sintaxis.py',52),
  ('comparison_production -> comparison_value','comparison_production',1,'p_comparison_production','sintaxis.py',59),
  ('comparison_production -> comparison_value comparison comparison_production','comparison_production',3,'p_comparison_production','sintaxis.py',60),
  ('comparison_value -> value comparison value','comparison_value',3,'p_comparison_value','sintaxis.py',65),
  ('logic_value -> value logic_operator value','logic_value',3,'p_logic_value','sintaxis.py',69),
  ('comparison -> LESS_THAN','comparison',1,'p_comparison','sintaxis.py',74),
  ('comparison -> GREATER_THAN','comparison',1,'p_comparison','sintaxis.py',75),
  ('comparison -> LESS_THAN_EQUAL','comparison',1,'p_comparison','sintaxis.py',76),
  ('comparison -> GREATER_THAN_EQUAL','comparison',1,'p_comparison','sintaxis.py',77),
  ('comparison -> NOT_EQUAL','comparison',1,'p_comparison','sintaxis.py',78),
  ('comparison -> EQUAL_EQUAL','comparison',1,'p_comparison','sintaxis.py',79),
  ('value -> INT','value',1,'p_value','sintaxis.py',85),
  ('value -> FLOAT','value',1,'p_value','sintaxis.py',86),
  ('value -> STRING','value',1,'p_value','sintaxis.py',87),
  ('value -> CHAR','value',1,'p_value','sintaxis.py',88),
  ('value -> BOOL','value',1,'p_value','sintaxis.py',89),
  ('value -> ID','value',1,'p_value','sintaxis.py',90),
  ('logic_operator -> AND','logic_operator',1,'p_logic_operator','sintaxis.py',96),
  ('logic_operator -> OR','logic_operator',1,'p_logic_operator','sintaxis.py',97),
  ('logic_operator -> NOT','logic_operator',1,'p_logic_operator','sintaxis.py',98),
]
