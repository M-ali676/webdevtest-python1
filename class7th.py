# name=
# roll=
# eng=
# maths=
# pys=
# chems=
# isla=
# obtain=
# total=
# per=
# if per>=70

print("*****Marksheet******")

name=input("Enter your full name")
roll=input("Enter your roll No.(1234:),(5678:)")
english=int(input("Enter English Marks"))
math=int(input("Enter Math Marks"))
chemstry=int(input("Enter Chemstry Marks"))
biology=int(input("Enter Biology Marks"))
physics=int(input("Enter Physics Marks"))
sindhi=int(input("Enter Sindhi Marks"))
obtainmarks=english+math+chemstry+biology+physics+sindhi
total=600
percentage=(obtainmarks/total)*100

if percentage >=80:
    print(f"You got A+  grade {percentage}%")
elif percentage >=70:
    print(f"You got A  grade {percentage}%")
elif percentage >=60:
    print("you got B grade {percentage}%")
elif percentage >=50:
    print("you got C grade {percentage}%")
elif percentage >=40:
    print("you got D grade {percentage}%")
elif percentage >=33:
    print("you got E grade {percentage}%")
else:
    print(f" Dear {name:}, You are fail/You are pass ")
