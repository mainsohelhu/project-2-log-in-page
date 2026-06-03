function greet(name,age) {
    console.log(`Hello, ${name}! You are ${age} years old.`);
}
person = greet("Alice", 30);

aadhar = {
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

function getDetals(num) {
    if(num in aadhar){
        return aadhar[num];
        
    }
}

id = getDetals(102)
console.log(id);