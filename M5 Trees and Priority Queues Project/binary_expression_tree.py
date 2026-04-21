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
        tokens = postfix_expression.split()
        for token in tokens:
            if token.isdigit():
                node = TreeNode(token)
                stack.push(node)

            elif token == '+' or token == '-' or token == '*' or token == '/':
                node = TreeNode(token)

                if not stack.is_empty():
                    right = stack.top()
                    stack.pop()
                    node.right = right
                else:
                    raise ValueError("Error - Stack is empty")

                
                if not stack.is_empty():
                    left = stack.top()
                    stack.pop()
                    node.left = left
                else:
                    raise ValueError("Error - Stack is empty")

                stack.push(node)

            else:
                raise ValueError("Error - Unsupported token: " + token)

        if not stack.is_empty():
            self.root = stack.top()
            stack.pop()
            
        else:
            raise ValueError("Error - Stack is empty")
        
        if not stack.is_empty():
            raise ValueError("Error - unused tokens left on the stack")

    def evaluate_tree(self):
        if self.root == None:
            raise ValueError("Error - Tree is empty. An empty tree cannot be evaluated.")
        return self.evaluate(self.root)

    def infix_traversal(self):
        if self.root == None:
            raise ValueError("Error - Tree is empty. An empty tree cannot be traversed.")

        tokens = []
        self._inorder(self.root, tokens)
        return " ".join(tokens)


    #Helper functions

    def _inorder(self, node, out):
        if node == None:
            return None

        else:
            out.append("(")
            self._inorder(node.left, out)
            out.append(str(node.value))
            self._inorder(node.right, out)
            out.append(")")


    def _evaluate(self, node):
        if node.left == None and node.right == None:
            return float(node.value)
        else:
            left_value = self._evaluate(node.left)
            right_value = self._evaluate(node.right)
            if node.value == '+':
                return left_value + right_value
            elif node.value == '-':
                return left_value - right_value
            elif node.value == '*':
                return left_value * right_value
            elif node.value == '/':
                if right_value == 0:
                    raise ValueError("Error - Division by zero")
                return left_value / right_value



