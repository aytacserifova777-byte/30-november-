temperatures=[-3,2,8,15,22,27,31]
for index,temp in enumerate(temperatures, start=1):
    if temp<0:
        print(f"{index}ci gun:{temp}saxta")
    elif temp<10:
        print(f"{index}ci gun {temp}:soyuq")
    elif temp<20:
        print(f"{index}ci gun {temp}:mulayim")
    elif temp<30:
        print(f"{index}ci gun {temp}:isti")
    elif temp>=30:
        print(f"{index}ci gun {temp}:cox isti")            