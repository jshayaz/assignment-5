my_dict={"Alice": 85, "shayaz":75,"avinash": 55}
a=str(input("Enter the student's name: "))
if a in my_dict:
    print(f"{a}'s marks : {my_dict[a]}")
else:
    print("Studnt not found.")
