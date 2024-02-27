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

name_list = ["Jagadeesh", "Jagan"]

# combining list and get dict by converting
Keys = ["Java", "Python", "Azure"]
Values = ["Programming", "DataScience", "Cloud"]

data_merge = dict(zip(Keys, Values))

print(data_merge)  # O/P: {'Java': 'Programming', 'Python': 'DataScience', 'Azure': 'Cloud'}

print(data_merge["Java"])  # we can retrieve index value of Java here . O/P: Programming

del (data_merge["Azure"])  # deletes the Azure Key Value Pair

print(data_merge)

# List and Dictionaries inside Dictionaries

inside_dict = {
    "Name": "Jagan",
    "Nickname": "Jagadeesh",
    "Companies_Worked": ["TCS", "Persistent"],
    "Tech_Stack": {"Cloud": "Azure", "Programming": ("Java", "Python"), "CICD": "Azure_Yaml",
                   "DevOps": {"Orchestration": "Kubernetes", "Image_Builds": "Docker"}}
}

print(inside_dict["Tech_Stack"])

print(inside_dict["Tech_Stack"]["DevOps"])

for i in inside_dict.keys():
    print(inside_dict.get(i))

count=0
# for i in inside_dict:
#     if(j==inside_dict[i]):
#         print(i+"is available")


# dev_resources=[]
# for  i in resources:
#     if i.name.endswith('dev'):
#         dev_respources.append(i)


#     dev_resources = [i for i in resources if i.name.endswith('dev')]


if data_dict["nickname"] == name_list[0]:
    print("Both are same")

else:
    print("Both are not same")
