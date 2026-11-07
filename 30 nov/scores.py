scores = [78, 92, 65, 88, 100, 54, 91, 73]
total =0
for bal in scores:
 total=total +bal
print ("cem:" , total) 
orta_bal = total / len(scores)
print(f"orta bal:{orta_bal} {total}/{len(scores)}={total/len(scores)}")
print(f"90-dən yuxarı bal olan tələbələrin sayı: {len([bal for bal in scores if bal >= 90])}")
print(f"en yuklsek bal: {max(scores)}")