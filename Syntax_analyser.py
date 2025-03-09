import re

class NeoASMSyntaxAnalyzer:
    def __init__(self):
        # Initialize the list to store the tokens
        self.tokens = []
        self.current_token = None
        self.position = 0  # Pointer for token position

    def tokenize(self, source_code):
        # Step 1: Tokenize the input source code using regex
        token_specifications = [
            ('VAR', r'VAR'),
            ('MAP', r'MAP'),
            ('AOT', r'AOT'),
            ('PACKET', r'PACKET'),
            ('INT', r'INT'),
            ('FLOAT', r'FLOAT'),
            ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),
            ('NUMBER', r'\d+'),
            ('RANGE', r'RANGE'),
            ('CHECK', r'CHECK'),
            ('ALIGNED', r'ALIGNED'),
            ('REGISTER', r'REGISTER'),
            ('EQUALS', r'='),
            ('COLON', r':'),
            ('COMMA', r','),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('WHITESPACE', r'\s+'),
            ('NEWLINE', r'\n'),
            ('OTHER', r'.'),
        ]

        # Create a combined regex pattern
        master_pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specifications)
        regex = re.compile(master_pattern)

        # Use finditer to tokenize the input string
        for match in regex.finditer(source_code):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE' and kind != 'NEWLINE':  # Ignore whitespace and newline
                self.tokens.append((kind, value))
        
        # Reset position to start parsing
        self.position = 0

    def advance(self):
        # Advance to the next token
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def expect(self, kind):
        # Ensure that the current token matches the expected kind
        if self.current_token[0] == kind:
            value = self.current_token[1]
            self.advance()
            return value
        else:
            raise SyntaxError(f"Expected {kind} but got {self.current_token[0]}")

    def parse(self):
        # Start parsing the source code into an AST
        self.advance()
        ast = []

        while self.current_token:
            if self.current_token[0] == 'VAR':
                ast.append(self.parse_variable())
            elif self.current_token[0] == 'MAP':
                ast.append(self.parse_map())
            elif self.current_token[0] == 'AOT':
                ast.append(self.parse_AOT())
            elif self.current_token[0] == 'PACKET':
                ast.append(self.parse_packet())
            else:
                self.advance()

        return ast

    def parse_variable(self):
        # Parse variable declarations
        self.expect('VAR')
        var_type = self.expect('IDENTIFIER')
        var_name = self.expect('IDENTIFIER')
        self.expect('RANGE')
        var_range = self.expect('NUMBER')
        self.expect('CHECK')
        var_check = self.expect('IDENTIFIER')

        # Memory alignment and register allocation will be handled later during code generation
        return {
            'type': 'variable',
            'var_type': var_type,
            'identifier': var_name,
            'attributes': {
                'range': var_range,
                'check': var_check
            }
        }

    def parse_map(self):
        # Parse map declarations
        self.expect('MAP')
        self.expect('LPAREN')
        src = self.expect('IDENTIFIER')
        self.expect('ARROW')
        dst = self.expect('IDENTIFIER')
        self.expect('RPAREN')

        return {
            'type': 'map',
            'identifier': src,
            'entries': [{'key': 'src', 'value': src}, {'key': 'dst', 'value': dst}]
        }

    def parse_AOT(self):
        # Parse AOT declarations
        self.expect('AOT')
        aot_name = self.expect('IDENTIFIER')
        self.expect('IDENTIFIER')  # Type
        aot_type = self.expect('IDENTIFIER')
        self.expect('NUMBER')  # Size
        size = self.expect('NUMBER')

        return {
            'type': 'AOT',
            'identifier': aot_name,
            'attributes': {'type': aot_type, 'size': size}
        }

    def parse_packet(self):
        # Parse packet declarations
        self.expect('PACKET')
        packet_name = self.expect('IDENTIFIER')
        self.expect('SIZE')
        size = self.expect('NUMBER')
        self.expect('EXEC')
        exec_mode = self.expect('IDENTIFIER')
        self.expect('PRIORITY')
        priority = self.expect('IDENTIFIER')

        return {
            'type': 'packet',
            'identifier': packet_name,
            'attributes': {
                'size': size,
                'exec': exec_mode,
                'priority': priority
            }
        }
