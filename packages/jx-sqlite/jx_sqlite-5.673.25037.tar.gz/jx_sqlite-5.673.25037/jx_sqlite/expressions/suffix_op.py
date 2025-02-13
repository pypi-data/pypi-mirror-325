# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://www.mozilla.org/en-US/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from jx_base.expressions import SuffixOp as SuffixOp_, FALSE, TRUE, SqlScript
from jx_sqlite.expressions.eq_op import EqOp
from jx_sqlite.expressions.length_op import LengthOp
from jx_sqlite.expressions.right_op import RightOp
from mo_sqlite import SQLang, check


class SuffixOp(SuffixOp_):
    @check
    def to_sql(self, schema) -> SqlScript:
        if not self.expr:
            return FALSE.to_sql(SQLang)
        elif self.suffix.missing(SQLang) is TRUE:
            return TRUE.to_sql(SQLang)
        else:
            return EqOp(RightOp(self.expr, LengthOp(self.suffix)), self.suffix).partial_eval(SQLang).to_sql(schema)
