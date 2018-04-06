
mySelf = {
    "name": "Jerome",
    "age": 25,
    "country": "New Jersey (Its a country, I promise)",
    "language": "Omgrofl"
}

def print_fun(obj):
    print("My name is {}. \nMy age is {}. \nI was born in the great wonderful country of {}. \nMy favorite lang is {}.".format(obj["name"], obj["age"], obj["country"], obj["language"]))

print_fun(mySelf)

# class User():
# #     name = "josh"
# #
# # print User().name

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def students_n_instructors(obj):
    print("Students")
    for i in range(0, len(obj["Students"])):
        name = obj["Students"][i]["first_name"] + ' ' + obj["Students"][i]["last_name"]
        print("{} - {} - {}".format(i+1, name, len(name)))
    print("Instructors")
    for i in range(0, len(obj["Instructors"])):
        name = obj["Instructors"][i]["first_name"] + ' ' + obj["Instructors"][i]["last_name"]
        print("{} - {} - {}".format(i + 1, name, len(name)))


students_n_instructors(users)