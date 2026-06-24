# รูปแบบของ  set

music_clud = {"Thawatchai","somchai","arnon"}
color = {"red","green","blue","doog"}
friut = {"orange","banana","watermelon","dog"}

#print ("nume", music_clud)
#print  (f"nume {music_clud}")

# union = ผลรวม (|)
all_member = music_clud|color|friut
print (f"nume {all_member}")

# intersection (&)
color_fruit = color & friut
print(f"nume {color_fruit}")

# difference ส่วนต่าง(-)
dif_color_fruit = friut - color
print (f"nume {dif_color_fruit}")

# symmetric difference
sym_color_fruit = color ^ friut
print (f"nume {sym_color_fruit}")

# การตรวจสอบสมาชิกอยู่ใน set หรือไม่
set_check = {"Thawatchai"}
if set_check.issubset(music_clud):
    print ("yes")
else:
    print ("no")