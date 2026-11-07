sifre = (input("sifre daxil edin:"))
boyuk=0
kicik=0
reqem =0
diger=0
for simvol in sifre:
    if simvol.isupper():
        boyuk+=1
    elif simvol.islower():
        kicik+=1
    elif simvol.isdigit():
        reqem+=1
    else:
        diger+=1    
print(f"boyuk herf: { boyuk}")
print(f"kicik herf :{kicik}")
print(f"reqem :{reqem}")
print(f"diger simvol:{diger}")
if len(sifre)>8 and boyuk>0 and kicik>0 and reqem >0 and diger >0:
    print("sifre gucludur")
else:   
    print("sifre zeifdir.") 
