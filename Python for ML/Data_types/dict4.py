#dict = {
      #"name"  : "Prabin",
      #"Cgpa"  : 9.6,
      #"marks" : [98, 89, 78],
#}

#print(dict)

#info = {
     #"name" : "Prabin Bhatt",
     #"Rollno" : 28,
     #"Age" : 21,
     #"Marks" :  [98,95,89]
     
#}
#print(info)

#Nested dictionary

student = {
      "name" : "Samir Bhatt",
      "Age" : 21,
      "Actors" : ["Akshay Kumar", "Shah Rukh Khan", "Salman Khan"], #list
      "Subjects" : ("Science", "Maths", "English", "Nepali"), #tuple
      98.4 : 45.5, #float value
      "score" : { #nested dict
          "Maths" : 78,
          "Science" : 87,
          "English" : 98,
      }
}
print(student.keys())
print(student.get("name"))


