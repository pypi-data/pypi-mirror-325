# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://www.mozilla.org/en-US/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from jx_base.expressions import ( SqlScript,
    StrictInOp as StrictInOp_,
    FALSE,
    Literal,
    ExistsOp,
    NestedOp,
    EqOp,
)
from jx_base.expressions.variable import is_variable
from jx_base.language import is_op
from mo_sqlite import SQLang
from mo_sqlite import check
from jx_sqlite.expressions._utils import value2boolean
from mo_sqlite.expressions.sql_script import SqlScript
from mo_json.types import JX_BOOLEAN
from mo_logs import Log
from mo_sql import ConcatSQL, SQL_IN
from mo_sqlite import quote_list
from mo_sqlite.expressions import SqlVariable


class StrictInOp(StrictInOp_):
    @check
    def to_sql(self, schema) -> SqlScript:
        value = self.value.partial_eval(SQLang).to_sql(schema)
        superset = self.superset.partial_eval(SQLang)
        if is_op(superset, Literal):
            values = superset.value
            if value.jx_type == JX_BOOLEAN:
                values = [value2boolean(v) for v in values]
            # TODO: DUE TO LIMITED BOOLEANS, TURN THIS INTO EqOp
            sql = ConcatSQL(value, SQL_IN, quote_list(values))
            return SqlScript(jx_type=JX_BOOLEAN, expr=sql, frum=self, miss=FALSE, schema=schema)

        if not is_variable(superset):
            Log.error("Do not know how to hanldle")

        sub_table = schema.get_table(superset.var)
        return ExistsOp(NestedOp(
            nested_path=sub_table.nested_path, where=EqOp(SqlVariable(None, "."), value.frum)
        )).to_sql(schema)
