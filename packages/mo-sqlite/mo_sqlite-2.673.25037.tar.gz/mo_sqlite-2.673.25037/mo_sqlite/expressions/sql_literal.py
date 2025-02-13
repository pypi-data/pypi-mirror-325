# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://www.mozilla.org/en-US/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from mo_future import extend

from jx_base.expressions import Literal as SqlLiteral, Literal
from mo_sql import SQL_EMPTY_STRING
from mo_sqlite.expressions._utils import SQL
from mo_sqlite.utils import quote_value

if SQL not in SqlLiteral.__bases__:
    SqlLiteral.__bases__ = SqlLiteral.__bases__ + (SQL,)


@extend(Literal)
def __iter__(self):
    yield from quote_value(self.value)


SQL_EMPTY_STRING.__class__ = SqlLiteral
SQL_EMPTY_STRING._value = ""
