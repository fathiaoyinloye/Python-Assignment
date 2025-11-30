
import unittest
from my_queue import MyQueue

class MyTestCase(unittest.TestCase):
    def test_that_queue_is_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())

    def test_that_one_element_is_added_my_queue_not_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        self.assertTrue(queue.myOffer("X"))
        self.assertFalse(queue.is_empty())


    def test_that_two_elements_are_added_to_my_queue_queue_not_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myOffer("X")
        self.assertTrue(queue.myOffer("Y"))
        self.assertFalse(queue.is_empty())

    def test_that_queue_is_full(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myOffer("X")
        queue.myOffer("Y")
        queue.myOffer("Z")
        queue.myOffer("X")
        queue.myOffer("Y")
        self.assertEqual(queue.myOffer("X"), False)

    def test_that_elementsXY_is_added_and_element_X_is_poll_off_the_queue(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myOffer("X")
        queue.myOffer("Y")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.myPoll(), "X")

    def test_thet_elementXYZ_is_added_and_elementXY_is_poll_off_the_queue_poll_returns_Y_as_last_element_polled(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myOffer("X")
        queue.myOffer("Y")
        queue.myOffer("Z")
        queue.myPoll()
        self.assertEqual(queue.myPoll(), "Y")

    def test_that_poll_returns_None_when_queue_is_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.myPoll(), None)

    def test_that_element_can_be_removed(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myAdd("X")
        queue.myAdd("Y")
        self.assertEqual(queue.myRemove(), "X")

    def test_that_two_elements_can_be_removed(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myAdd("X")
        queue.myAdd("Y")
        queue.myAdd("Z")
        queue.myRemove()
        self.assertEqual(queue.myRemove(), "Y")


    def test_that_remove_throws_error_when_queue_is_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        self.assertRaises(ValueError, queue.myRemove)

    def test_that_elements_are_added_and_first_element_can_be_checked(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myAdd("X")
        queue.myAdd("Y")
        queue.myAdd("Z")
        self.assertEqual(queue.element(), "X")

    def test_that_elements_are_added_and_removed_and_first_element_can_be_checked(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myAdd("X")
        queue.myAdd("Y")
        queue.myAdd("Z")
        queue.myAdd("J")
        queue.myRemove()
        queue.myRemove()
        self.assertEqual(queue.element(), "Z")

    def test_that_element_throws_error_when_queue_is_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        self.assertRaises(ValueError, queue.element)

    def test_that_that_first_element_can_be_peeked(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myAdd("X")
        queue.myAdd("Y")
        self.assertEqual(queue.peek(), "X")

    def test_that_elements_are_added_and_removed_and_first_element_can_be_peeked(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        queue.myAdd("X")
        queue.myAdd("Y")
        queue.myAdd("Z")
        queue.myAdd("J")
        queue.myRemove()
        self.assertEqual(queue.peek(), "Y")
        queue.myRemove()
        self.assertEqual(queue.peek(), "Z")

    def test_that_peek_returns_none_when_queue_is_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.peek(), None)




