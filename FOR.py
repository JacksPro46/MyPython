# n=int(input("Enter n"))
# list_m = []
# for i in range(n):
#    list_m.append(int(input()))
# print(max(list_m))

## Ex:1
for var in range(5):
   print(var)


## Ex:2 for loop with list

colors = ["Red", "Blue", "Green"]
for x in colors:
   print(x)
for y in range(len(colors)):
   print(colors[y])


## Ex:3 for loop with dict
   
inside_dict = {
    "Name": "Jagan",
    "Nickname": "Jagadeesh",
    "Companies_Worked": ["TCS", "Persistent"],
    "Tech_Stack": {"Cloud": "Azure", "Programming": ("Java", "Python"), "CICD": "Azure_Yaml",
                   "DevOps": {"Orchestration": "Kubernetes", "Image_Builds": "Docker"}}
}   

for x in inside_dict.values():
   print(x)

for y in inside_dict.keys():
   print(y)   

for i, j in inside_dict.items():
   print(i,j)