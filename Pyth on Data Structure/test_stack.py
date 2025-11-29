import unittest
from stack import MyStack


class TestStack(unittest.TestCase):
    def test_that_stack_is_empty(self):
        strings = MyStack()
        self.assertTrue(strings.is_empty())  # add assertion here

    def test_that_one_element_can_be_added_to_stack_and_stack_is_not_empty(self):
        strings = MyStack()
        strings.push("element")
        self.assertFalse(strings.is_empty())

    def test_that_two_elements_can_be_added_to_stack_and_stack_is_not_empty(self):
        strings = MyStack()
        strings.push("element")
        strings.push("second_element")
        self.assertFalse(strings.is_empty())
    def test_that_an_element_can_be_added_and_remove_in_the_stack_and_stack_is_empty(self):
        strings = MyStack()
        strings.push("element")
        strings.pop()
        self.assertTrue(strings.is_empty())

    def test_that_two_elements_can_be_added_and_one_removed_in_the_stack_and_stack_is_not_empty(self):
        strings = MyStack()
        strings.push("element")
        strings.push("second_element")
        strings.pop()
        self.assertFalse(strings.is_empty())

    def testThatAddTwoElements_popOneElement_MyStackNotEmpty_popLastElement(self):
        strings = MyStack()
        self.assertTrue(strings.is_empty())
        strings.push("element")
        strings.push("second_element")
        self.assertFalse(strings.is_empty())
        self.assertEqual("second_element", strings.pop())

    def testPeek_lastElementInTheStack(self):
        strings = MyStack()
        strings.push("element")
        strings.push("second_element")
        self.assertEqual(strings.peek(), "second_element")

    def testPopThrowsException_whenStackIsEmpty(self):
        strings = MyStack()
        self.assertRaises(TypeError, strings.pop)

    def test_stack_overflows_whenStackIsFull(self):
        strings = MyStack()
        strings.push("element")
        strings.push("second_element")
        strings.push("third_element")
        self.assertRaises(TypeError, strings.push("fourth_element"))

    def test_peek_throwsException_whenStackIsEmpty(self):
        strings = MyStack()
        self.assertRaises(TypeError, strings.peek)


