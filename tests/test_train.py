import unittest
from train import Train


class TrainTests(unittest.TestCase):
    def test_book_quote_and_cancel(self):
        train = Train(3)
        self.assertEqual(train.quote('Demo City A', 'Demo City B', 2), 1000)
        booking = train.book('Demo City A', 'Demo City B', 2)
        self.assertEqual(booking.fare, 1000)
        self.assertEqual(train.available_seats, 1)
        train.cancel(booking.reference)
        self.assertEqual(train.available_seats, 3)
        with self.assertRaises(ValueError):
            train.cancel(booking.reference)
        self.assertNotEqual(train.book('Demo City A', 'Demo City B').reference,
                            booking.reference)

    def test_overbooking_preserves_state(self):
        train = Train(3)
        train.book('Demo City A', 'Demo City B', 2)
        with self.assertRaises(ValueError):
            train.book('Demo City A', 'Demo City C', 2)
        self.assertEqual(train.available_seats, 1)

    def test_invalid_input_preserves_state(self):
        train = Train(3)
        for seats in [0, -1, 4, True, 1.5, '2']:
            with self.subTest(seats=seats), self.assertRaises(ValueError):
                train.book('Demo City A', 'Demo City B', seats)
        with self.assertRaises(ValueError):
            train.book('Unknown', 'Demo City B')
        self.assertEqual(train.available_seats, 3)

    def test_capacity_validation(self):
        for capacity in [0, -1, True, 2.5]:
            with self.subTest(capacity=capacity), self.assertRaises(ValueError):
                Train(capacity)


if __name__ == '__main__':
    unittest.main()
