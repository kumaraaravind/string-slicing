#String Slicing

name = "Aravind"
print(name[:])
print(name[1:5])
print(name[5:])
print(name[:4])
print(name[2:6])

#Neghative index
a = "kumar"
print(a[-4:-1])
print(a[:-4])
print(a[:-1])

#list data type
#implicit:
attendees =["Aravind","kumar","swami"]
print(type(attendees))
#explicit
attendees = list(("Aravind","kumar","swami"))
print(type(attendees))
#datatype/variable annotation
attendees:list = list(("Aravind","kumar","swami"))
print(type(attendees))
attendees:list = ["Aravind","kumar","swami"]
print(type(attendees))

#accesssing list item
attendees:list = ["Aravind","kumar","swami"]
print(attendees[0])
print(attendees[-2:])

#reverse a string
name = "Aravind"
print(name[::-1])

#reverse a string without slicing
a = "Aravind"
b = ""
for i in a:
    b = i+b
print(b)


#reverse of a list item
attendees:list = ["Aravind","kumar","swami"]
print(attendees[::-1])








