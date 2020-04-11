#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Token Types
# EOF shows end-of-file token
INTEGER, PLUS, MINUS, MUL, EOF = ('INTEGER', 'PLUS', 'MINUS', 'MUL', 'EOF')


# In[8]:


# Token class

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


# In[9]:


# Lexer

class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * -3 - 6"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        if self.current_char is '-':
            result += '-'
            self.advance()
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-' and self.text[self.pos+1].isspace():
                self.advance()
                return Token(MINUS, '-')
            
            if self.current_char == '-' and self.text[self.pos+1].isdigit():
                self.advance()
                return Token(INTEGER, -self.integer())

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            self.error()

        return Token(EOF, None)


# In[10]:


# A base node class called AST that other classes inherit from
class AST(object):
    pass

# A class to represent all binary operators (+,-,*)
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

# A class to hold an INTEGER token and the token’s value
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

# Parser
class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER | expr """
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        else:
            node = self.expr()
            return node

    def term(self):
        """term : factor ((MUL) factor)*"""
        node = self.factor()

        while self.current_token.type == MUL:
            token = self.current_token
            self.eat(MUL)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr   : term PLUS term | term MINUS term
        term   : factor MUL factor
        factor : INTEGER |  expr 
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()


# In[11]:


# This class visits and interprets the nodes of the AST
class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

# Interpreter 
class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        
    def visit_Num(self, node):
        return node.value
    
    # interpreter in the form of a function called eval
    def eval(self):
        tree = self.parser.parse()
        return self.visit(tree)


# In[12]:


def main():
    
    try:
        text = str(input())
    except TypeError:
        raise("Only arithmatic expression is allowed.")
    

    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.eval()
    print(int(result))


if __name__ == '__main__':
    main()


# In[ ]:




