
import unittest

from redsugar.utils import RedLexer


class TestRedLexer(unittest.TestCase):

    def setUp(self):
        self.source_code = """fn hello
print "hello world"
end
        """
        self.lexer = RedLexer(self.source_code)

    def tearDown(self):
        pass

    def test_tokenize(self):
        self.lexer.tokenize()
        self.assertEqual(self.lexer.tokens[0], '\n')
        self.assertEqual(self.lexer.tokens[2], 'fn')

    def test_remove_empty_tokens(self):
        self.assertNotIn('', self.lexer.tokens)

    def test_remove_newlines(self):
        self.assertNotIn('\n', self.lexer.tokens)
