from stack import Stack

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryExpressionTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    def clear_tree(self):
        self.root = None

    def build_from_postfix(self, postfix_expression):

        stack = Stack()
        for token in postfix_expression:
            if token.isdigit():
                node = TreeNode(token)
                stack.push(node)

            elif token == '+' or token == '-' or token == '*' or token == '/':
                node = TreeNode(token)

                if not stack.is_empty():
                    right = stack.peek()
                    stack.pop()
                    node.right = right

                    if not stack.is_empty():
