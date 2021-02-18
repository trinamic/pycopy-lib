# This file is part of the standard library of Pycopy project, minimalist
# and resource-efficient Python implementation.
#
# https://github.com/pfalcon/pycopy
# https://github.com/pfalcon/pycopy-lib
#
# The MIT License (MIT)
#
# Copyright (c) 2019-2020 Paul Sokolovsky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import uio
import ulogging
from opcode import opmap
from opcode import upyopcodes
from opcode import stack_effect
from ucodetype import CodeType, str2qstr
from mpylib import MPYWriter


log = ulogging.getLogger(__name__)


class AttrDict:

    def __init__(self, d):
        self.d = d

    def __getattr__(self, k):
        return self.d[k]


def get_opcode_ns():
    return AttrDict(opmap)


class Bytecode:

    def __init__(self, codeobjs_off=-1):
        self.buf = uio.BytesIO()
        self.co_names = []
        self.mpy_consts = []
        self.mpy_codeobjs = []
        self.codeobj_off = codeobjs_off
        self.labels = []
        self.stk_ptr = 0
        self.stk_use = 0
        self.exc_stk_ptr = 0
        self.exc_stk_use = 0
        self.co_flags = 0
        self.only_for_mpy = False

    def add(self, opcode, *args):
        delta = stack_effect(opcode, *args)
        self.stk_ptr += delta
        assert self.stk_ptr >= 0, self.stk_ptr
        if self.stk_ptr > self.stk_use:
            self.stk_use = self.stk_ptr

        self.buf.writebin("B", opcode)
        if args != ():
            arg = args[0]
        fl, extra = upyopcodes.mp_opcode_type(opcode)

        if opcode in (opmap["CALL_FUNCTION"], opmap["CALL_FUNCTION_VAR_KW"],
                      opmap["CALL_METHOD"], opmap["CALL_METHOD_VAR_KW"]):
            MPYWriter.write_uint(None, args[0] + (args[1] << 8), self.buf)
        elif opcode == opmap["LOAD_CONST_SMALL_INT"]:
            MPYWriter.write_int(None, arg, self.buf)
        elif opcode == opmap["LOAD_CONST_OBJ"]:
            MPYWriter.write_uint(None, len(self.mpy_consts), self.buf)
            self.mpy_consts.append(arg)
        elif opcode in (opmap["MAKE_FUNCTION"], opmap["MAKE_FUNCTION_DEFARGS"],
                        opmap["MAKE_CLOSURE"], opmap["MAKE_CLOSURE_DEFARGS"]):
            if self.codeobj_off >= 0:
                MPYWriter.write_uint(None, len(self.mpy_codeobjs) + self.codeobj_off, self.buf)
                self.mpy_codeobjs.append(arg)
            else:
                MPYWriter.write_uint(None, len(self.mpy_consts), self.buf)
                self.mpy_consts.append(arg)
            if opcode in (opmap["MAKE_CLOSURE"], opmap["MAKE_CLOSURE_DEFARGS"]):
                self.buf.writebin("B", args[1])
        elif opcode == opmap["RAISE_VARARGS"]:
            self.buf.writebin("B", arg)
        elif fl == upyopcodes.MP_OPCODE_OFFSET:
            self.buf.writebin("<H", arg)
        elif fl == upyopcodes.MP_OPCODE_QSTR:
            if self.only_for_mpy:
                self.buf.writebin("<H", 0)
            else:
                self.buf.writebin("<H", str2qstr(arg))
            # cache
            if opcode in upyopcodes.hascache:
                self.buf.writebin("B", 0)
            self.co_names.append(arg)
        elif fl == upyopcodes.MP_OPCODE_VAR_UINT:
            MPYWriter.write_uint(None, arg, self.buf)

        if opcode in (opmap["SETUP_EXCEPT"], opmap["SETUP_FINALLY"], opmap["SETUP_WITH"]):
            self.exc_stk_ptr += 1
            if self.exc_stk_ptr > self.exc_stk_use:
                self.exc_stk_use = self.exc_stk_ptr
        elif opcode == opmap["END_FINALLY"]:
            self.exc_stk_ptr -= 1

    def add_const(self, c):
        if self.codeobj_off >= 0:
            # add_const() is expected to be used to add function arg names, which
            # should happen before processing scope body (in particular, before
            # adding enclosed scopes (codeobjs)).
            assert not self.mpy_codeobjs
            self.codeobj_off += 1
        self.mpy_consts.append(c)

    def set_flag(self, fl):
        self.co_flags |= fl

    def get_label(self):
        label = len(self.labels)
        self.labels.append([None])
        return label

    # Put given label at the current position in instruction stream
    def put_label(self, label):
        self.labels[label][0] = self.buf.seek(0, 1)

    def jump(self, opcode, label):
        self.add(opcode, 0)
        self.labels[label].append(self.buf.seek(0, 1))

    def load_int(self, val):
        if -16 <= val <= 47:
            self.add(0x80 + val)
        else:
            self.add(opmap["LOAD_CONST_SMALL_INT"], val)

    def fastlocal_op(self, opcode, no):
        if no < 16:
            if opcode == opmap["LOAD_FAST_N"]:
                opcode = opmap["LOAD_FAST_MULTI"] + no
            elif opcode == opmap["STORE_FAST_N"]:
                opcode = opmap["STORE_FAST_MULTI"] + no
            elif opcode in (opmap["DELETE_FAST"], opmap["LOAD_DEREF"], opmap["STORE_DEREF"], opmap["DELETE_DEREF"]):
                # No "multi" form with implicit arg
                self.add(opcode, no)
                return
            else:
                assert 0
            self.add(opcode)
        else:
            self.add(opcode, no)

    def get_bc(self):
        if self.codeobj_off >= 0:
            assert len(self.mpy_consts) == self.codeobj_off, "consts: %d vs codeobj_off: %d" % (len(self.mpy_consts), self.codeobj_off)

        lab_id = 0
        for labl in self.labels:
            lab_pos = labl[0]
            assert lab_pos is not None, "Label #%d was not added to code" % lab_id
            for ref in labl[1:]:
                self.buf.seek(ref - 3)
                opcode = self.buf.readbin("B")
                rel = lab_pos - ref
                if opcode not in upyopcodes.has_forward_offset:
                    rel += 0x8000
                assert 0 <= rel <= 0xffff
                self.buf.writebin("<H", rel)
            lab_id += 1

        self.co_code = self.buf.getvalue()
        return self.co_code

    def get_codeobj(self):
        co = CodeType()
        co.co_code = self.get_bc()
        co.co_names = self.co_names
        co.co_consts = self.mpy_consts + self.mpy_codeobjs
        co.co_stacksize = co.mpy_stacksize = self.stk_use
        co.mpy_excstacksize = self.exc_stk_use
        co.co_flags = self.co_flags
        return co
