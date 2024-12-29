

#TOKENS
TT_PLUS = 'PLUS'
TT_SUB = 'SUB'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'


class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'        
        else:
            return f'{self.type}'
        

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1

        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_number(self):
        numStr = ''
        isDot = False

        while self.current_char!= None and self.current_char in '0123456789.':
            if self.current_char == '.':
                if isDot == False:
                    isDot = True
                    numStr += '.'
                else:
                    print('PLACEHOLDER FOR ERROR') #####################################
            else:
                numStr += self.current_char
            self.advance()

        if isDot:
            return Token(TT_FLOAT, float(numStr))
        else:
            return Token(TT_INT, int(numStr))



    def makeTokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char in '0123456789.':
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_SUB))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            else:
                #ERROR
                print('PLACEHOLDER FOR ERROR') #####################################
                self.advance()
        return tokens

def run(text):
    lexer = Lexer(text)
    tokens = lexer.makeTokens()

    return tokens
