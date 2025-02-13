# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://www.mozilla.org/en-US/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from jx_base.expressions import RightOp as _RightOp, ZERO
from jx_base.expressions._utils import simplified
from jx_sqlite.expressions._utils import SQLang
from jx_sqlite.expressions.strict_substring_op import StrictSubstringOp
from jx_sqlite.expressions.length_op import LengthOp
from jx_sqlite.expressions.max_op import MaxOp
from jx_sqlite.expressions.min_op import MinOp
from jx_sqlite.expressions.sub_op import SubOp


class RightOp(_RightOp):
    @simplified
    def partial_eval(self, lang):
        value = self.value.partial_eval(SQLang)
        length = self.length.partial_eval(SQLang)
        max_length = LengthOp(value)

        return StrictSubstringOp(value, MaxOp(ZERO, MinOp(max_length, SubOp(max_length, length))), max_length,)
