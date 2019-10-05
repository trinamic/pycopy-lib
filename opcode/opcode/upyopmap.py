# This file is autogenerated
# This file is a part of pycopy-lib project, https://github.com/pfalcon/pycopy-lib
opmap = {
"BINARY_ADD": 0xf2,
"BINARY_AND": 0xef,
"BINARY_EQUAL": 0xd9,
"BINARY_EXCEPTION_MATCH": 0xdf,
"BINARY_FLOOR_DIVIDE": 0xf6,
"BINARY_IN": 0xdd,
"BINARY_IS": 0xde,
"BINARY_LESS": 0xd7,
"BINARY_LESS_EQUAL": 0xda,
"BINARY_LSHIFT": 0xf0,
"BINARY_MAT_MULTIPLY": 0xf5,
"BINARY_MODULO": 0xf8,
"BINARY_MORE": 0xd8,
"BINARY_MORE_EQUAL": 0xdb,
"BINARY_MULTIPLY": 0xf4,
"BINARY_NOT_EQUAL": 0xdc,
"BINARY_OP_MULTI": 0xd7,
"BINARY_OR": 0xed,
"BINARY_POWER": 0xf9,
"BINARY_RSHIFT": 0xf1,
"BINARY_SUBTRACT": 0xf3,
"BINARY_TRUE_DIVIDE": 0xf7,
"BINARY_XOR": 0xee,
"BUILD_LIST": 0x51,
"BUILD_MAP": 0x53,
"BUILD_SET": 0x56,
"BUILD_SLICE": 0x58,
"BUILD_TUPLE": 0x50,
"CALL_FUNCTION": 0x64,
"CALL_FUNCTION_VAR_KW": 0x65,
"CALL_METHOD": 0x66,
"CALL_METHOD_VAR_KW": 0x67,
"DELETE_DEREF": 0x29,
"DELETE_FAST": 0x28,
"DELETE_GLOBAL": 0x2b,
"DELETE_NAME": 0x2a,
"DUP_TOP": 0x30,
"DUP_TOP_TWO": 0x31,
"END_FINALLY": 0x41,
"FOR_ITER": 0x43,
"GET_ITER": 0x42,
"GET_ITER_STACK": 0x47,
"IMPORT_FROM": 0x69,
"IMPORT_NAME": 0x68,
"IMPORT_STAR": 0x6a,
"INPLACE_ADD": 0xe5,
"INPLACE_AND": 0xe2,
"INPLACE_FLOOR_DIVIDE": 0xe9,
"INPLACE_LSHIFT": 0xe3,
"INPLACE_MAT_MULTIPLY": 0xe8,
"INPLACE_MODULO": 0xeb,
"INPLACE_MULTIPLY": 0xe7,
"INPLACE_OR": 0xe0,
"INPLACE_POWER": 0xec,
"INPLACE_RSHIFT": 0xe4,
"INPLACE_SUBTRACT": 0xe6,
"INPLACE_TRUE_DIVIDE": 0xea,
"INPLACE_XOR": 0xe1,
"JUMP": 0x35,
"JUMP_IF_FALSE_OR_POP": 0x39,
"JUMP_IF_TRUE_OR_POP": 0x38,
"LOAD_ATTR": 0x1d,
"LOAD_BUILD_CLASS": 0x20,
"LOAD_CONST_FALSE": 0x10,
"LOAD_CONST_NONE": 0x11,
"LOAD_CONST_OBJ": 0x17,
"LOAD_CONST_SMALL_INT": 0x14,
"LOAD_CONST_SMALL_INT_MULTI": 0x70,
"LOAD_CONST_STRING": 0x16,
"LOAD_CONST_TRUE": 0x12,
"LOAD_DEREF": 0x1a,
"LOAD_FAST_MULTI": 0xb0,
"LOAD_FAST_N": 0x19,
"LOAD_GLOBAL": 0x1c,
"LOAD_METHOD": 0x1e,
"LOAD_NAME": 0x1b,
"LOAD_NULL": 0x18,
"LOAD_SUBSCR": 0x21,
"LOAD_SUPER_METHOD": 0x1f,
"MAKE_CLOSURE": 0x62,
"MAKE_CLOSURE_DEFARGS": 0x63,
"MAKE_FUNCTION": 0x60,
"MAKE_FUNCTION_DEFARGS": 0x61,
"POP_EXCEPT_JUMP": 0x44,
"POP_JUMP_IF_FALSE": 0x37,
"POP_JUMP_IF_TRUE": 0x36,
"POP_TOP": 0x32,
"RAISE_VARARGS": 0x5c,
"RETURN_VALUE": 0x5b,
"ROT_THREE": 0x34,
"ROT_TWO": 0x33,
"SETUP_EXCEPT": 0x3f,
"SETUP_FINALLY": 0x40,
"SETUP_WITH": 0x3d,
"STORE_ATTR": 0x26,
"STORE_COMP": 0x57,
"STORE_DEREF": 0x23,
"STORE_FAST_MULTI": 0xc0,
"STORE_FAST_N": 0x22,
"STORE_GLOBAL": 0x25,
"STORE_MAP": 0x54,
"STORE_NAME": 0x24,
"STORE_SUBSCR": 0x27,
"UNARY_INVERT": 0xd2,
"UNARY_NEGATIVE": 0xd1,
"UNARY_NOT": 0xd3,
"UNARY_OP_MULTI": 0xd0,
"UNARY_POSITIVE": 0xd0,
"UNPACK_EX": 0x5a,
"UNPACK_SEQUENCE": 0x59,
"UNWIND_JUMP": 0x46,
"WITH_CLEANUP": 0x3e,
"YIELD_FROM": 0x5e,
"YIELD_VALUE": 0x5d,
}

opname = [
# 0x00
None, None, None, None, None, None, None, None, 
# 0x08
None, None, None, None, None, None, None, None, 
# 0x10
'LOAD_CONST_FALSE', 'LOAD_CONST_NONE', 'LOAD_CONST_TRUE', None, 'LOAD_CONST_SMALL_INT', None, 'LOAD_CONST_STRING', 'LOAD_CONST_OBJ', 
# 0x18
'LOAD_NULL', 'LOAD_FAST_N', 'LOAD_DEREF', 'LOAD_NAME', 'LOAD_GLOBAL', 'LOAD_ATTR', 'LOAD_METHOD', 'LOAD_SUPER_METHOD', 
# 0x20
'LOAD_BUILD_CLASS', 'LOAD_SUBSCR', 'STORE_FAST_N', 'STORE_DEREF', 'STORE_NAME', 'STORE_GLOBAL', 'STORE_ATTR', 'STORE_SUBSCR', 
# 0x28
'DELETE_FAST', 'DELETE_DEREF', 'DELETE_NAME', 'DELETE_GLOBAL', None, None, None, None, 
# 0x30
'DUP_TOP', 'DUP_TOP_TWO', 'POP_TOP', 'ROT_TWO', 'ROT_THREE', 'JUMP', 'POP_JUMP_IF_TRUE', 'POP_JUMP_IF_FALSE', 
# 0x38
'JUMP_IF_TRUE_OR_POP', 'JUMP_IF_FALSE_OR_POP', None, None, None, 'SETUP_WITH', 'WITH_CLEANUP', 'SETUP_EXCEPT', 
# 0x40
'SETUP_FINALLY', 'END_FINALLY', 'GET_ITER', 'FOR_ITER', 'POP_EXCEPT_JUMP', None, 'UNWIND_JUMP', 'GET_ITER_STACK', 
# 0x48
None, None, None, None, None, None, None, None, 
# 0x50
'BUILD_TUPLE', 'BUILD_LIST', None, 'BUILD_MAP', 'STORE_MAP', None, 'BUILD_SET', 'STORE_COMP', 
# 0x58
'BUILD_SLICE', 'UNPACK_SEQUENCE', 'UNPACK_EX', 'RETURN_VALUE', 'RAISE_VARARGS', 'YIELD_VALUE', 'YIELD_FROM', None, 
# 0x60
'MAKE_FUNCTION', 'MAKE_FUNCTION_DEFARGS', 'MAKE_CLOSURE', 'MAKE_CLOSURE_DEFARGS', 'CALL_FUNCTION', 'CALL_FUNCTION_VAR_KW', 'CALL_METHOD', 'CALL_METHOD_VAR_KW', 
# 0x68
'IMPORT_NAME', 'IMPORT_FROM', 'IMPORT_STAR', None, None, None, None, None, 
# 0x70
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0x78
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0x80
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0x88
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0x90
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0x98
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0xa0
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0xa8
'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 'LOAD_CONST_SMALL_INT', 
# 0xb0
'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 
# 0xb8
'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 'LOAD_FAST_MULTI', 
# 0xc0
'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 
# 0xc8
'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 'STORE_FAST_MULTI', 
# 0xd0
'UNARY_POSITIVE', 'UNARY_NEGATIVE', 'UNARY_INVERT', 'UNARY_NOT', None, None, None, 'BINARY_LESS', 
# 0xd8
'BINARY_MORE', 'BINARY_EQUAL', 'BINARY_LESS_EQUAL', 'BINARY_MORE_EQUAL', 'BINARY_NOT_EQUAL', 'BINARY_IN', 'BINARY_IS', 'BINARY_EXCEPTION_MATCH', 
# 0xe0
'INPLACE_OR', 'INPLACE_XOR', 'INPLACE_AND', 'INPLACE_LSHIFT', 'INPLACE_RSHIFT', 'INPLACE_ADD', 'INPLACE_SUBTRACT', 'INPLACE_MULTIPLY', 
# 0xe8
'INPLACE_MAT_MULTIPLY', 'INPLACE_FLOOR_DIVIDE', 'INPLACE_TRUE_DIVIDE', 'INPLACE_MODULO', 'INPLACE_POWER', 'BINARY_OR', 'BINARY_XOR', 'BINARY_AND', 
# 0xf0
'BINARY_LSHIFT', 'BINARY_RSHIFT', 'BINARY_ADD', 'BINARY_SUBTRACT', 'BINARY_MULTIPLY', 'BINARY_MAT_MULTIPLY', 'BINARY_FLOOR_DIVIDE', 'BINARY_TRUE_DIVIDE', 
# 0xf8
'BINARY_MODULO', 'BINARY_POWER', None, None, None, None, None, None, 
]

op_implicit_arg = [
# 0x00
None, None, None, None, None, None, None, None, 
# 0x08
None, None, None, None, None, None, None, None, 
# 0x10
None, None, None, None, None, None, None, None, 
# 0x18
None, None, None, None, None, None, None, None, 
# 0x20
None, None, None, None, None, None, None, None, 
# 0x28
None, None, None, None, None, None, None, None, 
# 0x30
None, None, None, None, None, None, None, None, 
# 0x38
None, None, None, None, None, None, None, None, 
# 0x40
None, None, None, None, None, None, None, None, 
# 0x48
None, None, None, None, None, None, None, None, 
# 0x50
None, None, None, None, None, None, None, None, 
# 0x58
None, None, None, None, None, None, None, None, 
# 0x60
None, None, None, None, None, None, None, None, 
# 0x68
None, None, None, None, None, None, None, None, 
# 0x70
-16, -15, -14, -13, -12, -11, -10, -9, 
# 0x78
-8, -7, -6, -5, -4, -3, -2, -1, 
# 0x80
0, 1, 2, 3, 4, 5, 6, 7, 
# 0x88
8, 9, 10, 11, 12, 13, 14, 15, 
# 0x90
16, 17, 18, 19, 20, 21, 22, 23, 
# 0x98
24, 25, 26, 27, 28, 29, 30, 31, 
# 0xa0
32, 33, 34, 35, 36, 37, 38, 39, 
# 0xa8
40, 41, 42, 43, 44, 45, 46, 47, 
# 0xb0
0, 1, 2, 3, 4, 5, 6, 7, 
# 0xb8
8, 9, 10, 11, 12, 13, 14, 15, 
# 0xc0
0, 1, 2, 3, 4, 5, 6, 7, 
# 0xc8
8, 9, 10, 11, 12, 13, 14, 15, 
# 0xd0
None, None, None, None, None, None, None, None, 
# 0xd8
None, None, None, None, None, None, None, None, 
# 0xe0
None, None, None, None, None, None, None, None, 
# 0xe8
None, None, None, None, None, None, None, None, 
# 0xf0
None, None, None, None, None, None, None, None, 
# 0xf8
None, None, None, None, None, None, None, None, 
]

op_stack_effect = [
# 0x00
None, None, None, None, None, None, None, None, 
# 0x08
None, None, None, None, None, None, None, None, 
# 0x10
1, 1, 1, None, 1, None, 1, 1, 
# 0x18
1, 1, 1, 1, 1, 1, 1, 1, 
# 0x20
1, 1, -1, -1, -1, -1, -1, -1, 
# 0x28
None, None, None, None, None, None, None, None, 
# 0x30
None, None, None, None, None, None, None, None, 
# 0x38
None, None, None, None, None, None, None, None, 
# 0x40
None, None, None, None, None, None, None, None, 
# 0x48
None, None, None, None, None, None, None, None, 
# 0x50
None, None, None, None, -1, None, None, -1, 
# 0x58
None, None, None, None, None, None, None, None, 
# 0x60
None, None, None, None, None, None, None, None, 
# 0x68
None, None, None, None, None, None, None, None, 
# 0x70
1, 1, 1, 1, 1, 1, 1, 1, 
# 0x78
1, 1, 1, 1, 1, 1, 1, 1, 
# 0x80
1, 1, 1, 1, 1, 1, 1, 1, 
# 0x88
1, 1, 1, 1, 1, 1, 1, 1, 
# 0x90
1, 1, 1, 1, 1, 1, 1, 1, 
# 0x98
1, 1, 1, 1, 1, 1, 1, 1, 
# 0xa0
1, 1, 1, 1, 1, 1, 1, 1, 
# 0xa8
1, 1, 1, 1, 1, 1, 1, 1, 
# 0xb0
1, 1, 1, 1, 1, 1, 1, 1, 
# 0xb8
1, 1, 1, 1, 1, 1, 1, 1, 
# 0xc0
-1, -1, -1, -1, -1, -1, -1, -1, 
# 0xc8
-1, -1, -1, -1, -1, -1, -1, -1, 
# 0xd0
0, 0, 0, 0, None, None, None, -1, 
# 0xd8
-1, -1, -1, -1, -1, -1, -1, -1, 
# 0xe0
-1, -1, -1, -1, -1, -1, -1, -1, 
# 0xe8
-1, -1, -1, -1, -1, -1, -1, -1, 
# 0xf0
-1, -1, -1, -1, -1, -1, -1, -1, 
# 0xf8
-1, -1, None, None, None, None, None, None, 
]
