students = [("Aysel", 95), ("Murad", 72), ("Leyla", 84), ("Elvin", 48), ("Nigar", 63)]
for student in students:
    name,grade=student
    if grade>=90:
        print(f"{name}","A")
    elif grade>=80:
        print(f"{name}","B")
    elif grade>=70:
        print(f"{name}","C")
    elif grade>=60:
        print(f"{name}","D")
    elif grade>=50:
        print(f"{name}","E") 
    elif grade<50:
        print(f"{name}","F")               