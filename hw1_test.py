import data
import hw1
import unittest


class TestCases(unittest.TestCase):
    # Part 1: vowel_count
    def test_vowel_count_1(self):
        self.assertEqual(hw1.vowel_count("hello"), 2)

    def test_vowel_count_2(self):
        self.assertEqual(hw1.vowel_count("AEIOUaeiou"), 10)

    # Part 2: short_lists
    def test_short_lists_1(self):
        self.assertEqual(hw1.short_lists([[1, 2], [3], [4, 5, 6], [7, 8]]), [[1, 2], [7, 8]])

    def test_short_lists_2(self):
        self.assertEqual(hw1.short_lists([[1], [2, 3], [4]]), [[2, 3]])

    # Part 3: ascending_pairs
    def test_ascending_pairs_1(self):
        self.assertEqual(hw1.ascending_pairs([[3, 1], [4, 2, 3], [5, 8]]), [[1, 3], [4, 2, 3], [5, 8]])

    def test_ascending_pairs_2(self):
        self.assertEqual(hw1.ascending_pairs([[2, 2], [5, 1], [9]]), [[2, 2], [1, 5], [9]])

    # Part 4: add_prices
    def test_add_prices_1(self):
        price1 = data.Price(5, 75)
        price2 = data.Price(3, 50)
        self.assertEqual(hw1.add_prices(price1, price2), data.Price(9, 25))

    def test_add_prices_2(self):
        price1 = data.Price(10, 99)
        price2 = data.Price(0, 1)
        self.assertEqual(hw1.add_prices(price1, price2), data.Price(11, 0))

    # Part 5: rectangle_area
    def test_rectangle_area_1(self):
        rect = data.Rectangle(data.Point(1, 5), data.Point(4, 1))
        self.assertEqual(hw1.rectangle_area(rect), 12.0)

    def test_rectangle_area_2(self):
        rect = data.Rectangle(data.Point(0, 10), data.Point(5, 5))
        self.assertEqual(hw1.rectangle_area(rect), 25.0)

    # Part 6: books_by_author
    def test_books_by_author_1(self):
        book1 = data.Book(["Author A"], "Book 1")
        book2 = data.Book(["Author B"], "Book 2")
        books = [book1, book2]
        self.assertEqual(hw1.books_by_author("Author A", books), [book1])

    def test_books_by_author_2(self):
        book1 = data.Book(["Author A", "Author B"], "Book 1")
        book2 = data.Book(["Author C"], "Book 2")
        books = [book1, book2]
        self.assertEqual(hw1.books_by_author("Author B", books), [book1])

    # Part 7: circle_bound
    def test_circle_bound_1(self):
        rect = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        expected_circle = data.Circle(data.Point(1, 1), 1.4142135623730951)
        self.assertEqual(hw1.circle_bound(rect), expected_circle)

    def test_circle_bound_2(self):
        rect = data.Rectangle(data.Point(1, 5), data.Point(4, 1))
        expected_circle = data.Circle(data.Point(2.5, 3), 2.5)
        self.assertEqual(hw1.circle_bound(rect), expected_circle)

    # Part 8: below_pay_average
    def test_below_pay_average_1(self):
        # Assuming you have an Employee class with pay_rate attribute
        employees = [
            data.Employee("Alice", 30000),
            data.Employee("Bob", 50000),
            data.Employee("Charlie", 20000)
        ]

        # Call the function with the employees list
        self.assertEqual(hw1.below_pay_average(employees), ["Alice", "Charlie"])

    def test_below_pay_average_2(self):
        emp1 = data.Employee("Alice", 70000)  # 70,000
        emp2 = data.Employee("Bob", 80000)  # 80,000
        emp3 = data.Employee("Charlie", 90000)  # 90,000
        employees = [emp1, emp2, emp3]

        # Alice earns below average (which is 76,666.67)
        self.assertEqual(hw1.below_pay_average(employees), ["Alice"])


if __name__ == '__main__':
    unittest.main()
