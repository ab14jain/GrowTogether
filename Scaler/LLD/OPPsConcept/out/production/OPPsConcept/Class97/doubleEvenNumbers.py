def is_even(num):
    return num % 2 == 0


def double(num):
    return num * 2

# TODO: Implement the function below
def filter_and_double_even_numbers(numbers):
    # code here
    even_num = filter(is_even, numbers)
    db = list(map(double, even_num))
    return db

print(filter_and_double_even_numbers([1,2,3,4,5,6,7,8]))
    