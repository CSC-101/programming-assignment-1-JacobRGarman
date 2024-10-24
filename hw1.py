import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(s: str) -> int:
    """
    Count the number of vowels in the input string.

    :param s: A string to be analyzed for vowels.
    :return: The count of vowels (a, e, i, o, u) in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Part 2
def short_lists(lst: list[list[int]]) -> list[list[int]]:
    """
    Return a new list containing only the sublists of length 2.

    :param lst: A list of lists of integers.
    :return: A new list consisting of sublists that are of length 2.
    """
    return [sublist for sublist in lst if len(sublist) == 2]

# Part 3
def ascending_pairs(lst: list[list[int]]) -> list[list[int]]:
    """
    Return a new list with nested lists of length 2 sorted in ascending order.

    :param lst: A list of lists of integers.
    :return: A new list where sublists of length 2 are sorted; others are unchanged.
    """
    return [sorted(sublist) if len(sublist) == 2 else sublist for sublist in lst]

# Part 4
def add_prices(p1: data.Price, p2: data.Price) -> data.Price:
    """
    Compute the sum of two Price objects and return a new Price object.

    :param p1: The first Price object.
    :param p2: The second Price object.
    :return: A new Price object representing the total of p1 and p2.
    """
    total_cents = p1.cents + p2.cents
    total_dollars = p1.dollars + p2.dollars + total_cents // 100
    return data.Price(total_dollars, total_cents % 100)

# Part 5
def rectangle_area(rect: data.Rectangle) -> float:
    """
    Calculate the area of a rectangle given its corners.

    :param rect: A Rectangle object defined by two Point objects.
    :return: The area of the rectangle.
    """
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    return width * height

# Part 6
def books_by_author(author_name: str, books: list[data.Book]) -> list[data.Book]:
    """
    Return a list of books written by the specified author.

    :param author_name: The name of the author to search for.
    :param books: A list of Book objects to search within.
    :return: A list of Book objects authored by author_name.
    """
    return [book for book in books if author_name in book.authors]

# Part 7
def circle_bound(rect: data.Rectangle) -> data.Circle:
    """
    Compute the smallest bounding circle for a given rectangle.

    :param rect: A Rectangle object.
    :return: A Circle object representing the bounding circle for the rectangle.
    """
    center_x = (rect.top_left.x + rect.bottom_right.x) / 2
    center_y = (rect.top_left.y + rect.bottom_right.y) / 2
    center = data.Point(center_x, center_y)

    # Calculate the distance from the center to any corner
    radius = ((rect.bottom_right.x - center_x) ** 2 + (rect.bottom_right.y - center_y) ** 2) ** 0.5
    return data.Circle(center, radius)

# Part 8
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    """
    Identify employees who are paid less than the average pay.

    :param employees: A list of Employee objects.
    :return: A list of names of employees with pay rates below the average.
    """
    total_salary = sum(emp.pay_rate for emp in employees)  # Use pay_rate
    average_salary = total_salary / len(employees) if employees else 0
    return [emp.name for emp in employees if emp.pay_rate < average_salary]
