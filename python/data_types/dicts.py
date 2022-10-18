# dictionaies

person_0 = {
    "name" : "Matt Cunningham",
    "age" : 22,
    "sex" : "Male",
    "friends" : ["Matt", "Garrett"],
    "float_value" : 123.456
}

person_1 = {
    "name" : "Matt Cunningham",
    "age" : 22,
    "sex" : "Male",
    "friends" : [person_0],
    "float_value" : 123.456
}

person_2 = {
    "name" : "Michael Munson",
    "age" : 22,
    "sex" : "Male",
    "friends" : [person_1, person_0],
    "float_value" : 123.456,
    "login_info" : {
        "username" : "bigbutts",
        "password" : "************"
        }
}

print(
    person_2["login_info"]["username"],
    person_1["friends"]
)