# Copyright (c) 2023, NVIDIA CORPORATION. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum

from legate_dataframe.lib.core.column import LogicalColumn

class unary_operator(Enum): ...

def unary_operation(col: LogicalColumn, op: unary_operator) -> LogicalColumn: ...