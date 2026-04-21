# Binary Expression Tree Test Program

from binary_expression_tree import BinaryExpressionTree

#Test data from Canvas
postfix_expressions = [
    "5 3 +",
    "8 2 - 3 +",
    "5 3 8 * +",
    "6 2 / 3 +",
    "5 8 + 3 -",
    "5 3 + 8 *",
    "8 2 3 * + 6 -",
    "5 3 8 * + 2 /",
    "8 2 + 3 6 * -",
    "5 3 + 8 2 / -"
]

print("----- Binary Expression Tree ----")

for expression in postfix_expressions:
    tree = BinaryExpressionTree()
    tree.build_from_postfix(expression)

    infix = tree.infix_traversal()
    postfix = tree.postfix_traversal()
    value = tree.evaluate_tree()

    print(f"Infix Expression: {infix}")
    print(f"Postfix Expression: {postfix}")
    print(f"Evaluated Result: {value}")

