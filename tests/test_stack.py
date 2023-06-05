import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.stack, ['data1', 'data2'])
        stack.push('data3')
        self.assertEqual(stack.stack, ['data1', 'data2', 'data3'])


if __name__ == '__main__':
    unittest.main()
