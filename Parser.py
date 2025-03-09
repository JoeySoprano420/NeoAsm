class NeoASMParser:
    def __init__(self, tokens):
        self.tokens = tokens  # List of tokens
        self.position = 0  # Current position in token list
        self.ast = []  # Abstract Syntax Tree

    def parse(self):
        while self.position < len(self.tokens):
            token = self.tokens[self.position]

            if token == "map":
                self.ast.append(self.parse_map_declaration())
            elif token == "var":
                self.ast.append(self.parse_variable_declaration())
            elif token == "AOT":
                self.ast.append(self.parse_AOT_declaration())
            elif token == "pkt":
                self.ast.append(self.parse_packetized_execution())
            else:
                raise SyntaxError(f"Unexpected token: {token}")

            self.position += 1

        return self.ast

    def parse_map_declaration(self):
        self.position += 1  # Skip 'map' token
        identifier = self.tokens[self.position]  # Expecting map identifier
        self.position += 1

        if self.tokens[self.position] != "{":
            raise SyntaxError("Expected '{' after map identifier")
        self.position += 1  # Skip '{'

        map_entries = []
        while self.tokens[self.position] != "}":
            key = self.tokens[self.position]
            self.position += 1
            if self.tokens[self.position] != ":":
                raise SyntaxError("Expected ':' in map entry")
            self.position += 1  # Skip ':'
            value = self.tokens[self.position]
            map_entries.append((key, value))
            self.position += 1
            if self.tokens[self.position] == ",":
                self.position += 1  # Skip ','

        self.position += 1  # Skip '}'
        return {"type": "map", "identifier": identifier, "entries": map_entries}

    def parse_variable_declaration(self):
        self.position += 1  # Skip 'var' token
        var_type = self.tokens[self.position]
        self.position += 1
        identifier = self.tokens[self.position]
        self.position += 1

        if self.tokens[self.position] != "{":
            raise SyntaxError("Expected '{' after variable declaration")
        self.position += 1  # Skip '{'

        attributes = {}
        while self.tokens[self.position] != "}":
            if self.tokens[self.position] == "range:":
                self.position += 1
                attributes["range"] = self.tokens[self.position]
            elif self.tokens[self.position] == "check:":
                self.position += 1
                attributes["check"] = self.tokens[self.position]
            self.position += 1

        self.position += 1  # Skip '}'
        return {"type": "variable", "var_type": var_type, "identifier": identifier, "attributes": attributes}

    def parse_AOT_declaration(self):
        self.position += 1  # Skip 'AOT' token
        identifier = self.tokens[self.position]  # Expecting AOT identifier
        self.position += 1

        if self.tokens[self.position] != "{":
            raise SyntaxError("Expected '{' after AOT identifier")
        self.position += 1  # Skip '{'

        attributes = {}
        while self.tokens[self.position] != "}":
            if self.tokens[self.position] == "STATIC" or self.tokens[self.position] == "SOFT" or self.tokens[self.position] == "RIGID":
                attributes["type"] = self.tokens[self.position]
            elif self.tokens[self.position] == "size:":
                self.position += 1
                attributes["size"] = self.tokens[self.position]
            self.position += 1

        self.position += 1  # Skip '}'
        return {"type": "AOT", "identifier": identifier, "attributes": attributes}

    def parse_packetized_execution(self):
        self.position += 1  # Skip 'pkt' token
        identifier = self.tokens[self.position]  # Expecting packet identifier
        self.position += 1

        if self.tokens[self.position] != "{":
            raise SyntaxError("Expected '{' after packet identifier")
        self.position += 1  # Skip '{'

        attributes = {}
        while self.tokens[self.position] != "}":
            if self.tokens[self.position] == "size:":
                self.position += 1
                attributes["size"] = self.tokens[self.position]
            elif self.tokens[self.position] == "exec:":
                self.position += 1
                attributes["exec"] = self.tokens[self.position]
            elif self.tokens[self.position] == "priority:":
                self.position += 1
                attributes["priority"] = self.tokens[self.position]
            self.position += 1

        self.position += 1  # Skip '}'
        return {"type": "packet", "identifier": identifier, "attributes": attributes}
