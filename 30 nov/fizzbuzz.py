eded = int(input("eded daxil edin:"))
if eded<0:
    print(f"menfi ededin faktoriali yoxdur")
else:
    faktorial=1
    for i in range(1,eded+1):
        faktorial=faktorial*i
    print(f"faktorial: {faktorial}")
