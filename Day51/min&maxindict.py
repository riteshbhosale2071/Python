def find():
    Students = {"Ram" : 23, "Shyam" : 34, "Krishna": 18}
    max = Students["Ram"]

    for name,age in Students.items():

        if age > max:
            max = age
            max_name = name

    print("Max:",max_name)

    min = Students["Ram"]

    for name,age in Students.items():
        if age < min:
            min = age
            min_name = name
            
    print("Min:",min_name)

find()