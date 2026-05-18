#!/usr/bin/env python3
"""quick-math-cli – evaluate a single arithmetic expression.

Usage:
    ./calc.py "2 + 3 * (4 - 1)"
"""

import ast
import operator as op
import sys

# Supported operators mapping
allowed_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}

def eval_expr(node):
    """Recursively evaluate an AST node representing a safe arithmetic expression."""
    if isinstance(node, ast.Num):  # < Python 3.8
        return node.n
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise TypeError(f"Unsupported constant type: {type(node.value)}")
    if isinstance(node, ast.BinOp):
        left = eval_expr(node.left)
        right = eval_expr(node.right)
        op_type = type(node.op)
        if op_type in allowed_operators:
            return allowed_operators[op_type](left, right)
        raise TypeError(f"Unsupported binary operator: {op_type}")
    if isinstance(node, ast.UnaryOp):
        operand = eval_expr(node.operand)
        op_type = type(node.op)
        if op_type in allowed_operators:
            return allowed_operators[op_type](operand)
        raise TypeError(f"Unsupported unary operator: {op_type}")
    if isinstance(node, ast.Expression):
        return eval_expr(node.body)
    raise TypeError(f"Unsupported AST node: {type(node)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: ./calc.py \"<expression>\"")
        sys.exit(1)
    expr = sys.argv[1]
    try:
        parsed = ast.parse(expr, mode='eval')
        result = eval_expr(parsed)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
