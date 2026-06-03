class student:
    name = "sohel"
    age = 20

s1 = student()
print(s1.name,s1.age)

class dog:
    name = "tommmy"

d1 = dog()
print(d1.name)

# class person:
#     def __init__(self,list):

#         self.list_of_students = list = { 
#             "student1":{
#             "name" : "sohel",
#             "age" : 24,
#             "cls" : "12th"
#             },
#             "student2":{
#                 "name" : "raju",
#                 "age" : 24,
#                 "cls" : "10th"
#             }
#             }
#     def show(self):
#         if (self.name == "sohel" and self.age == 24):
#             print("wellcome home sir")
#             print("Name : " ,self.name)
#             print("Age : ", self.age)
#             print("Class : " , self.cls)
#         else:
#             print("Who the fuck are you you son of a bitch")

# p1 = person(input("Enter your name :- "),int(input("Enater age :- ")),input("Enter class name :- "))
# p1.show()

adhar = {
    101:{
        "name" : "sohel",
        "age" : 24,
        "address" : "Changorabhatha raipur cg"
    },
    102:{
        "name" : "ishrat khan",
        "age" : 24,
        "address" : "khamtarai raipur cg",
        "dob" : "25/12/2002"
    },
    103:{
         "name" : "roshan",
         "age" : 25
    },
    104:{
         "name" : "ketu",
         "age" : 10
    },
    105:{
         "name" : "rahu",
         "age" : 20
    }
}
print(105 in adhar)

def get_results(roll):
        if (roll in adhar):
            return adhar[roll]
        else:
             return "roll numebr not found please recheck it"


roll_num = get_results(int(input("Enter your roll number :- ")))
print(roll_num)

