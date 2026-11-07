soz=input("soz ve ya cumle daxil edin:")
saitler = "aeəıioöuü"
say=0 
for herf in soz:
    if herf in saitler:
     say=say+1
print("saitlerin sayi:", say)
