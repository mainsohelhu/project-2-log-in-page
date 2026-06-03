a = 10
b = 3
print(a|b)

print(~99)
print(~-100)

student = {
    101 :{
        "name" : "sohel",
        "age" : 20
    },
    102 :{
        "name" : "khusi",
        "age" : 10
    },
    103 :{
        "name" : "manu",
        "age" : 20
    }
}

def get_details(num):
    if (num in student):
        print(student[num])

roll = get_details(int(input("Enter you roll number")))