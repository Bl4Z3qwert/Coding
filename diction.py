# ?empty dict>
print('name.class,school,age')
student={
    "name":'John', "age": 12, "class":8 ,"school":'Robotics And ML Int', "movie": "It", "sport":'volleyball',"country":'Great Britain',"gender":'male'
}
print(student["country"])
student.pop('movie')
print(student)