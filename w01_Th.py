# Dictionry
phone_book = {}
phone_book02 = dict()

# สร้างค่าใน Dict
student = {
    "name" : "Thawatchai",
    "Gender": "Barm",
    "age": 28,
    "tel": "090-088-0909090"
}

#print (student["name"])
#name_student = student.get("name","ไม่มีข้อมูล")
#print(name_student)

class_room ={
    "room_nume": "p01",
    "Capacity": 28,
    "equipment":["com","por","mi"],

   "teacher":{
    "nume":"Thawatchai",
    "sudject":"por",
    "tel":"090-088-0909090"
    } 
}


class_room_check = class_room.get("room_nume","ไม่มีข้อมูล")

# ลบค่า dict
del student["age"]
data_pop = student.pop ("get","no data") #pop คือการดึงข้อมูลออกมา

print(student)