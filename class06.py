# Decisions in python
# -- implementation of logical operators:

#  online Clothe Recommendation System

# print("*****Online  Clothing Store*****")
# name=input("Enter your name:")
# email=input("Enter your email:")
# budget=int(input("Enter your budget (Minimum spanding limit 5000):"))
# 
# if budget<5000 and budget>=2000:
#     print(f"Dear{name}, as per your budget: this is {budget}, we recommend you for causal wears")
# elif budget >=5000 and budget <10000:
#     print(f"Dear{name}, as per your budget: this is {budget}, we recommend you semi- causal wears")
# elif budget >=10000 and budget <20000:
#     print(f"Dear{name}, as per your budget: this is {budget}, we recommend you for party wears")
# elif budget >=20000 and budget <30000:
#     print(f"Dear{name}, as per your budget: this is {budget}, we recommend you for semi-formal wears")
# elif budget >=30000:
#     print(f"Dear{name}, as per your budget: this is {budget}, we recommend you for a formal category along with and all kind wears")
# else:
#     print(f"Dear{name}, as per your budget: this is {budget}, we recommend you to go home")

# 
# print("*****Online  Smartphone Store*****")
# name=input("Enter your name:")
# email=input("Enter your email:")
# budget=int(input("Enter your budget:"))
# camera=int(input("Enter a megapixel of camera you want? for ex:(50, 80, 100)"))
# inernalStorage=int(input ("Enter internalstorage in gb you want ? for ex:(64, 128, 256, 512)"))
# fp=input=("Do want fingerprint feature? (yes/no)")
# 
# 
# if camera==50 and internalstorage==64 and fp=="no":
#     print(f"Dear{name}, as per your requirements, you will have these phonesspecific budget \n1.Samsung A20 (Rs.20000), \n.2 Infinix Note 8 (Rs.22000)  \n3. Motrolla (Rs.25000)")
# elif camera==80 and internalstorage==64 or fp=="yes":
#     print(f"Dear {name}, as per your requirements you will have these phones under specific budget \n1. Samsung S8 (Rs.26000), \n2.Samsung Note 11(Rs.28000)")
# elif camera==80 and internalstorage==128 or fp=="yes":
#     print(f"Dear {name}, as per your requirements you will have these phones under specific budget \n1. Samsung S8 (Rs.29000), \n2.Samsung Note 11(Rs.32000)")
# elif camera==80 and internalstorage==256 or fp=="yes":
#     print(f"Dear {name}, as per your requirements you will have these phones under specific budget \n1. Samsung S8 (Rs.36000), \n2.Samsung Note 11(Rs.38000)")
# else:
#     print(f"Dear{name},invalid your budget: ")

# code a python programe for one of yhe car shorome , that shorome needs an online presence so that store ask from user related to budget ,
# car type, engine cc, sitting capacity and about gear and sunroof so the online porta recomended him/her a suitable car.

print("******Online Cars ******")
name=input("Enter your name ")
email=input("Enter your email ")
budget=int(input("Enter your budget"))
cartype=input("Enter car Type: Press according\n. for suv \n. For Sedan \n. Enter preference:")
cc=int(input("Enter Engine capacity, (CC):"))
seating_capacity=int(input("Enter seat capacity, "))
gear=input("Enter your gera type , for example (auto/manual)")
sunroof=input("Sunroof Available or not (yes/no")

if (budget >= 1000000 and budget<=1500000) and cc<=1000 and gear == "manual" and sunroof=="no" and seats <=5 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Suzuki Alto \n2. Daihatsu \n3. Suzuki Mehran")
   
elif (budget >15000000 and budget<=3000000) and cc<=1300 and gear == "manual" and sunroof=="no" and seats <=5 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Honda city(mouse) \n2. Toyota corrolla(saloon) \n3. Suzuki Liana")
   
elif (budget> 3000000 and budget<=4500000) and cc<=2000 and gear == "auto" and sunroof=="yes" and seats <=5 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Honda Civic \n2. MG 5 \n3. Kia stonic")

elif (budget>=500000 and budget<1000000) and cc<=800 and gear == "manual" and sunroof=="no" and seats <=4 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Charade \n2. FX \n3. coure ")
elif (budget<500000) and cc<600 and gear == "manual" and sunroof=="no" and seats <=4 and cartype==2:
    print(f"Dear {name}, Please increase your budget")        

else:
    print(f"Dear {name}, urf Baray log! Recommended Cars for you: \n1. Land cruiser \n2. Prado \n3.Lexus LX 570 \n4. Fortuner \n5. Pajero")
    
 

