#ERRORS
class Errors:
    def __init__(self, error_name, details, pos_start, pos_end):
        self.error_name = error_name
        self.details = details
        self.pos_start = pos_start
        self.pos_end = pos_end

    def print_error(self):
        result = f'{self.error_name}: {self.details}, at (line:{self.pos_start.ln+1} :: col:{self.pos_start.col+1})'
        return result

class IllegalCharacterError(Errors):
    def __init__(self, details, pos_start, pos_end):
        super().__init__('Illegal Character', details, pos_start, pos_end)

    

#POSITIONS
class Position:
    def __init__(self, idx, ln, col):
        self.idx = idx
        self.ln = ln
        self.col = col
    
    def advance(self, current_char):
        self.idx += 1
        self.col += 1
        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self
    
    def copy(self):
        return Position(self.idx, self.ln, self.col)




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
        self.pos = Position(-1, 0, -1)
        self.current_char = None
        self.advance()
        self.errors_list = []

    def advance(self):
        self.pos.advance(current_char = self.current_char)

        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

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
                pos_start = self.pos.copy()

                illegal_char = self.current_char
                self.advance()

                return [], IllegalCharacterError(" " + illegal_char + " ", pos_start, self.pos)


        return tokens, None

def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.makeTokens()

    return tokens, errors
