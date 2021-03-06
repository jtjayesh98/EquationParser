
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSleftEXPONENTCOSINE DIVIDE EQUALS EXPONENT FLOAT INT LN LOG LPAREN MINUS PLUS RPAREN SINE SQRT SYMBOL TAN TIMES VARIABLENAMEstatement : expression EQUALS expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EXPONENT expressionexpression : MINUS expression %prec UMINUSexpression : LOG LPAREN expression RPAREN\n                  | LN LPAREN expression RPAREN\n                  | SQRT LPAREN expression RPAREN\n                  | SINE LPAREN expression RPAREN\n                  | COSINE LPAREN expression RPAREN\n                  | TAN LPAREN expression RPARENexpression : LPAREN expression RPARENexpression : FLOATexpression : INTexpression : VARIABLENAMEexpression : SYMBOL'
    
_lr_action_items = {'MINUS':([0,2,3,5,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[3,17,3,3,-15,-16,-17,-18,3,3,3,3,3,3,-7,3,17,3,3,3,3,3,17,-2,-3,-4,-5,-6,17,-14,17,17,17,17,17,-8,-9,-10,-11,-12,-13,]),'LOG':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'LN':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'SQRT':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'SINE':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'COSINE':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'TAN':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'LPAREN':([0,3,4,5,6,7,8,9,10,15,16,17,18,19,20,22,24,25,26,27,28,],[5,5,22,5,24,25,26,27,28,5,5,5,5,5,5,5,5,5,5,5,5,]),'FLOAT':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'INT':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'VARIABLENAME':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'SYMBOL':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'$end':([1,11,12,13,14,21,29,30,31,32,33,34,36,42,43,44,45,46,47,],[0,-15,-16,-17,-18,-7,-1,-2,-3,-4,-5,-6,-14,-8,-9,-10,-11,-12,-13,]),'EQUALS':([2,11,12,13,14,21,30,31,32,33,34,36,42,43,44,45,46,47,],[15,-15,-16,-17,-18,-7,-2,-3,-4,-5,-6,-14,-8,-9,-10,-11,-12,-13,]),'PLUS':([2,11,12,13,14,21,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[16,-15,-16,-17,-18,-7,16,16,-2,-3,-4,-5,-6,16,-14,16,16,16,16,16,-8,-9,-10,-11,-12,-13,]),'TIMES':([2,11,12,13,14,21,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[18,-15,-16,-17,-18,-7,18,18,18,18,-4,-5,-6,18,-14,18,18,18,18,18,-8,-9,-10,-11,-12,-13,]),'DIVIDE':([2,11,12,13,14,21,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[19,-15,-16,-17,-18,-7,19,19,19,19,-4,-5,-6,19,-14,19,19,19,19,19,-8,-9,-10,-11,-12,-13,]),'EXPONENT':([2,11,12,13,14,21,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[20,-15,-16,-17,-18,20,20,20,20,20,20,20,-6,20,-14,20,20,20,20,20,-8,-9,-10,-11,-12,-13,]),'RPAREN':([11,12,13,14,21,23,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-15,-16,-17,-18,-7,36,-2,-3,-4,-5,-6,42,-14,43,44,45,46,47,-8,-9,-10,-11,-12,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,5,15,16,17,18,19,20,22,24,25,26,27,28,],[2,21,23,29,30,31,32,33,34,35,37,38,39,40,41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression EQUALS expression','statement',3,'p_statement_assign','eqparser.py',162),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','eqparser.py',171),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','eqparser.py',172),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','eqparser.py',173),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','eqparser.py',174),
  ('expression -> expression EXPONENT expression','expression',3,'p_expression_binop','eqparser.py',175),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','eqparser.py',179),
  ('expression -> LOG LPAREN expression RPAREN','expression',4,'p_expression_single_fun','eqparser.py',183),
  ('expression -> LN LPAREN expression RPAREN','expression',4,'p_expression_single_fun','eqparser.py',184),
  ('expression -> SQRT LPAREN expression RPAREN','expression',4,'p_expression_single_fun','eqparser.py',185),
  ('expression -> SINE LPAREN expression RPAREN','expression',4,'p_expression_single_fun','eqparser.py',186),
  ('expression -> COSINE LPAREN expression RPAREN','expression',4,'p_expression_single_fun','eqparser.py',187),
  ('expression -> TAN LPAREN expression RPAREN','expression',4,'p_expression_single_fun','eqparser.py',188),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','eqparser.py',192),
  ('expression -> FLOAT','expression',1,'p_expression_float','eqparser.py',196),
  ('expression -> INT','expression',1,'p_expression_int','eqparser.py',200),
  ('expression -> VARIABLENAME','expression',1,'p_expression_name','eqparser.py',204),
  ('expression -> SYMBOL','expression',1,'p_expression_symbol','eqparser.py',208),
]
