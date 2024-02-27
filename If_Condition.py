data_dict = {

    "name": "Jagan",
    "nickname": "Jagadeesh"
}

print(data_dict["nickname"])

name_list = ["Jagadeesh", "Jagan"]

if data_dict["nickname"] != name_list[0]:
    print("Both values are same")

elif data_dict["name"] == name_list[1]:
    print(data_dict["name"] +" & "+ name_list[1] + " "+"are same values")

else:
    print("Both are not same") 