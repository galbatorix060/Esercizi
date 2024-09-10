import unittest

def anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())

class TestAnagramFunction(unittest.TestCase):
    def classico(self):
        self.assertTrue(anagram("listen", "silent"))