import pandas as pd
import numpy as np
import random
import string
import datetime


# ----------------------------------------
# DATAFRAME FUNCTIONS
# ----------------------------------------
def get_sample_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
        "Salary": [50000, 60000, 70000, 80000]
    }
    return pd.DataFrame(data)


def get_large_random_dataframe(rows=100, cols=10):
    data = np.random.randint(1, 1000, size=(rows, cols))
    columns = [f"Column_{i+1}" for i in range(cols)]
    return pd.DataFrame(data, columns=columns)


def get_time_series_dataframe():
    dates = pd.date_range(start='1/1/2020', periods=365, freq='D')
    values = np.random.randn(365)
    return pd.DataFrame({"Date": dates, "Value": values})


def get_dataframe_with_nan(rows=10, cols=5):
    data = np.random.randn(rows, cols)
    data[data > 1] = np.nan
    columns = [f"Column_{i+1}" for i in range(cols)]
    return pd.DataFrame(data, columns=columns)


def get_dataframe_with_duplicates():
    data = {
        "ID": [1, 2, 2, 3, 4, 4, 4],
        "Name": ["Alice", "Bob", "Bob", "Charlie", "David", "David", "David"]
    }
    return pd.DataFrame(data)


def get_categorical_dataframe():
    data = {
        "Category": ["A", "B", "C", "A", "B", "C"],
        "Values": np.random.randint(10, 100, size=6)
    }
    return pd.DataFrame(data)


def get_people_dataframe(rows=10):
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "London", "Berlin", "Tokyo", "Sydney",
              "Dubai"]
    ages = np.random.randint(18, 60, rows)
    salaries = np.random.randint(30000, 150000, rows)
    occupations = ["Engineer", "Doctor", "Artist", "Lawyer", "Teacher", "Scientist", "Pilot", "Chef", "Athlete",
                   "Musician"]

    data = {
        "Name": [random.choice(names) for _ in range(rows)],
        "City": [random.choice(cities) for _ in range(rows)],
        "Age": ages,
        "Salary": salaries,
        "Occupation": [random.choice(occupations) for _ in range(rows)]
    }
    return pd.DataFrame(data)


def get_animal_dataframe(rows=10):
    animals = ["Dog", "Cat", "Elephant", "Tiger", "Lion", "Giraffe", "Penguin", "Dolphin", "Bear", "Wolf"]
    habitats = ["Forest", "Savannah", "Ocean", "Jungle", "Desert", "Arctic", "Mountain", "Swamp", "Cave", "Grassland"]
    weights = np.random.randint(10, 500, rows)
    lifespans = np.random.randint(5, 80, rows)

    data = {
        "Animal": [random.choice(animals) for _ in range(rows)],
        "Habitat": [random.choice(habitats) for _ in range(rows)],
        "Weight_kg": weights,
        "Lifespan_years": lifespans
    }
    return pd.DataFrame(data)


def get_colors_dataframe(rows=10):
    colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Purple", "Orange", "Pink", "Brown"]
    hex_codes = ["#FF0000", "#0000FF", "#008000", "#FFFF00", "#000000", "#FFFFFF", "#800080", "#FFA500", "#FFC0CB",
                 "#A52A2A"]
    brightness = ["Light", "Dark", "Medium"]

    data = {
        "Color": [random.choice(colors) for _ in range(rows)],
        "HexCode": [random.choice(hex_codes) for _ in range(rows)],
        "Brightness": [random.choice(brightness) for _ in range(rows)]
    }
    return pd.DataFrame(data)


def get_fruit_dataframe(rows=10):
    fruits = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grapes", "Mango", "Orange", "Peach", "Strawberry"]
    colors = ["Red", "Yellow", "Green", "Orange", "Purple", "Blue"]
    prices = np.random.uniform(1, 10, rows)

    data = {
        "Fruit": [random.choice(fruits) for _ in range(rows)],
        "Color": [random.choice(colors) for _ in range(rows)],
        "Price": prices
    }
    return pd.DataFrame(data)


# ----------------------------------------
# SERIES FUNCTIONS
# ----------------------------------------
def get_sample_series():
    return pd.Series([10, 20, 30, 40, 50], name="Numbers")


def get_large_series(size=1000):
    return pd.Series(np.random.randn(size), name="Large Series")


def get_random_series(size=5):
    return pd.Series(np.random.randint(1, 100, size=size), name="Random Numbers")


def get_city_series(size=10):
    cities = ["New York", "London", "Tokyo", "Berlin", "Sydney", "Paris", "Rome", "Moscow", "Beijing", "Cairo"]
    return pd.Series(random.choices(cities, k=size), name="Cities")


def get_animal_series(size=10):
    animals = ["Dog", "Cat", "Tiger", "Elephant", "Penguin", "Wolf", "Dolphin", "Giraffe", "Rabbit", "Fox"]
    return pd.Series(random.choices(animals, k=size), name="Animals")


# ----------------------------------------
# DICTIONARY FUNCTIONS
# ----------------------------------------
def get_sample_dict():
    return {"name": "John Doe", "age": 28, "city": "New York"}


def get_nested_dict():
    return {"person": {"name": "Alice", "age": 25}, "job": {"title": "Engineer", "salary": 70000}}


def get_random_dict():
    keys = ["".join(random.choices(string.ascii_uppercase, k=5)) for _ in range(5)]
    values = np.random.randint(1, 100, size=5).tolist()
    return dict(zip(keys, values))


def get_random_person_dict():
    first_names = ["John", "Emma", "Liam", "Sophia", "Noah", "Olivia", "William", "Ava", "James", "Isabella"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Lee", "Harris", "Clark", "Lewis", "Walker"]
    return {
        "FullName": f"{random.choice(first_names)} {random.choice(last_names)}",
        "Age": random.randint(18, 65),
        "City": random.choice(["New York", "Paris", "Tokyo", "Berlin", "Dubai"]),
        "Job": random.choice(["Engineer", "Doctor", "Teacher", "Artist", "Scientist"])
    }


def get_food_prices_dict():
    foods = ["Pizza", "Burger", "Sushi", "Pasta", "Tacos", "Salad", "Steak", "Soup", "Cake", "Ice Cream"]
    return {food: round(random.uniform(5, 25), 2) for food in foods}


# ----------------------------------------
# LIST FUNCTIONS
# ----------------------------------------
def get_sample_list():
    return [1, 2, 3, 4, 5]


def get_nested_list():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def get_large_list(size=1000):
    return [random.randint(1, 1000) for _ in range(size)]


def get_mixed_type_list():
    return ["Alice", 42, 3.14, True, None, {"key": "value"}, [1, 2, 3]]


def get_human_names_list():
    return ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]


def get_city_list():
    return ["New York", "Los Angeles", "London", "Berlin", "Tokyo", "Paris", "Rome", "Moscow", "Beijing", "Cairo"]


def get_animal_list():
    return ["Dog", "Cat", "Tiger", "Elephant", "Penguin", "Wolf", "Dolphin", "Giraffe", "Rabbit", "Fox"]


def get_date_list(start_date="2020-01-01", num_days=10):
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    return [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_days)]


def get_time_series_dict():
    dates = get_date_list(num_days=30)
    values = np.random.randn(30).tolist()
    return dict(zip(dates, values))


def get_random_coordinates_list(size=10):
    return [{"latitude": round(random.uniform(-90, 90), 6), "longitude": round(random.uniform(-180, 180), 6)} for _ in range(size)]


def info():
    print("Module Created By Bhavya Soni For Quickly Getting Various Data Structures For Teaching and Testing Purposes")
