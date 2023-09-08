# Dictionaries are type of Key Value pairs format with {}

data = {1: "Jagan", 2: "Mohan",
        3: "Krishna", 4: "Gudela"}

print(data[3], data[4])

print(data.get(2))

data_dict = {

    "name": "Jagan",
    "nickname": "Jagadeesh"
}

print(data_dict["nickname"])

# combining list and get dict by converting
Keys = ["Java", "Python", "Azure"]
Values = ["Programming", "DataScience", "Cloud"]

data_merge = dict(zip(Keys, Values))

print(data_merge)  # O/P: {'Java': 'Programming', 'Python': 'DataScience', 'Azure': 'Cloud'}
