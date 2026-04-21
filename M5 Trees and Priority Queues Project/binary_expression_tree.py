from stack import Stack

#Class: TreeNode
#Purpose: A node in a binary expression tree, which can represent either an operator or an operand. Each node has a value, and references to left and right child nodes.
#Paramters: value (str) - The value of the node, which can be an operator ('+', '-', '*', '/') or an operand (a number as a string).
#Returns: None
#Preconditions: The value should be a valid operator or operand.
#Postconditions: A TreeNode object is created with the specified value and no children.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Class: BinaryExpressionTree
#Purpose: A binary expression tree that can be built from a postfix expression and evaluated.
#Paramters: None
#Returns: None
#Preconditions: None
#Postconditions: A BinaryExpressionTree object is created with no root.
class BinaryExpressionTree:

    #Method: __init__
    #Purpose: Initializes a BinaryExpressionTree object with no root.
    #Parameters: None
    #Returns: None
    #Preconditions: None
    #Postconditions: A BinaryExpressionTree object is created with no root.
    def __init__(self):
        self.root = None

    #Method: is_empty
    #Purpose: Checks if the binary expression tree is empty (a tree is empty if it has no root).
    #Parameters: None
    #Returns: True if the tree is empty, False otherwise
    #Preconditions: None
    #Postconditions: None
    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    #Method: clear_tree
    #Purpose: Clears the binary expression tree by setting the root to None.
    #Parameters: None
    #Returns: None
    #Preconditions: None
    #Postconditions: The binary expression tree is cleared and has no root.
    def clear_tree(self):
        self.root = None

    #Method: build_from_postfix
    #Purpose: Builds a binary expression tree from a given postfix expression. This method uses a stack to keep track of the nodes while constructing the tree.
    #Parameters:
    # - str postfix_expression
    #Returns: None
    #Preconditions: The postfix expression should is a valid whitespace-separated postfix expression (tokens = numbersor + - * /).
    #Postconditions: An expression tree representing the postfix expression is built.
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

    #Method: evaluate_tree
    #Purpose: Evaluates the binary expression tree and returns the result. This method uses a helper function to recursively evaluate the tree.
    #Parameters: None
    #Returns: The result of evaluating the expression tree.
    #Preconditions: The tree is not empty.
    #Postconditions: The expression tree is evaluated and the result is returned.
    def evaluate_tree(self):
        if self.root == None:
            raise ValueError("Error - Tree is empty. An empty tree cannot be evaluated.")
        return self._evaluate(self.root)

    #Method: infix_traversal
    #Purpose: Returns a string representation of the infix traversal of the binary expression tree. This method uses a helper function to recursively traverse the tree in infix order.
    #Parameters: None
    #Returns: A string representation of the infix traversal of the tree.
    #Preconditions: The tree is not empty.
    #Postconditions: The infix traversal of the tree is returned as a string with parentheses.
    def infix_traversal(self):
        if self.root == None:
            raise ValueError("Error - Tree is empty. An empty tree cannot be traversed.")

        tokens = []
        self._inorder(self.root, tokens)
        return " ".join(tokens)

    #Method: postfix_traversal
    #Purpose: Returns a string representation of the postfix traversal of the binary expression tree. This method uses a helper function to recursively traverse the tree in postorder.
    #Parameters: None
    #Returns: A string representation of the postfix traversal of the tree.
    #Preconditions: The tree is not empty.
    #Postconditions: The postfix traversal of the tree is returned as a space-separated string.
    def postfix_traversal(self):
        if self.root == None:
            raise ValueError("Error - Tree is empty. An empty tree cannot be traversed.")
        tokens = []
        self._postorder(self.root, tokens)
        return " ".join(tokens)


    #Helper functions

    #Helper function: _inorder
    #Purpose: A helper function for infix_traversal that recursively traverses the tree in infix order and appends the tokens to the output list.
    #Parameters:
    # - TreeNode node: The current node being traversed.
    # - list out: The list to which the tokens are appended during the traversal.
    #Returns: None
    #Preconditions: The node is a valid TreeNode and the out list is initialized.
    #Postconditions: out contains infix representation of subtree.
    def _inorder(self, node, out):

        if node == None:
            return None

        elif node.left == None and node.right == None:
            out.append(str(node.value))
            return None

        else:
            out.append("(")
            self._inorder(node.left, out)
            out.append(str(node.value))
            self._inorder(node.right, out)
            out.append(")")

    #Helper function: _postorder
    #Purpose: A helper function for postfix_traversal that recursively traverses the tree in postorder and appends the tokens to the output list.
    #Parameters:
    # - TreeNode node: The current node being traversed.
    # - list out: The list to which the tokens are appended during the traversal.
    #Returns: None
    #Preconditions: The node is a valid TreeNode and the out list is initialized.
    #Postconditions: out contains postfix representation of subtree.
    def _postorder(self, node, out):
        if node == None:
            return None
        else:
            self._postorder(node.left, out)
            self._postorder(node.right, out)
            out.append(str(node.value))


    #Helper function: _evaluate
    #Purpose: A helper function for evaluate_tree that recursively evaluates the expression tree and returns the result.
    #Parameters:
    # - TreeNode node: The current node being evaluated.
    #Returns: The result of evaluating the subtree rooted at the given node.
    #Preconditions: The node is a valid TreeNode and the tree is properly constructed.
    #Postconditions: The subtree rooted at the given node is evaluated and the result is returned. Note that a division by zero error will be raised if the denominator evaluates to 0.
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



