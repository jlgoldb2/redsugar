
class RedSource(object):
    """
    The RedSource object represents the source code file and is
    responsible for the source file's IO and reference.

    The Source object shall present
    """
    def __init__(self, filename):
        self.text = self.read(filename)

    def read(self, filename):
        with open(filename, 'r') as f:
            return f.read()


class RedLexer(object):
    """
    Lexer tokenizes redsugar source.
    """
    def __init__(self, source):
        self.text = source

    def tokenize(self):
        self.tokens = self.text.split(' ')
        self.remove_empty_tokens()

    def remove_empty_tokens(self):
        if '' in self.tokens:
            self.tokens.remove('')
            self.remove_empty_tokens()
