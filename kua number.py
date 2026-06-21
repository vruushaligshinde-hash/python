#calculate kua number
def kua_number(dob,gender):
    year=int(dob[-4:])
    total=sum(int(d) for d in str(year))

    while total > 9:
        total = sum(int(d) for d in str(total))

    if gender == "male":
        kua = 11 - total 
    else:
        kua = total + 4

        while kua > 9:
            kua = sum(int(d) for d in str(kua))
    return kua

kua_category_directions = {
    "1":{
        "love":"south",
        "growth":"north",
        "health":"east",
        "wealth":"southwest",
        "avoid":"west,northeast,northwest,southwest",
        "donate":"food to poor on saturday"
    },
    "2":{
        "love":"northwest",
        "growth":"southwest",
        "health":"west",
        "wealth":"northeast",
        "avoid":"east,southeast,south",
        "donate":"give food/pulses to birds"
    },
    "3":{
        "love":"southeast",
        "growth":"east",
        "health":"north",
        "wealth":"south",
        "avoid":"southwest,northwest,northheast,west",
        "donate":"medicine to needy"
    },
    "4":{
        "love":"southwest",
        "growth":"southeast",
        "health":"south",
        "wealth":"north",
        "avoid":"northwest,west,northeast,southwest,northeast",
        "donate":"books for needy"
    },
    "5":{
        "love":"northwest",
        "growth":"southwest",
        "health":"west",
        "wealth":"northeast",
        "avoid":"east,southeast,south,north",
        "donate":"medicine to asthama paitents"
   },
    "6":{
        "love":"southwest",
        "growth":"northwest",
        "health":"northeast",
        "wealth":"west",
        "avoid":"east,southeast,south,north",
        "donate":"help in the marriage of poor"
    },
    "7":{
        "love":"northwest",
        "growth":"west",
        "health":"southwest",
        "wealth":"northwest",
        "avoid":"north,south,southeast,east",
        "donate":"medicine/food for blind people"
    },
    "8":{
        "love":"west",
        "growth":"northeast",
        "health":"northwest",
        "wealth":"southwest",
        "avoid":"south,north,east,southeast",
        "donate":"give food to religious places"
    },
    "9":{
        "love":"north",
        "growth":"south",
        "health":"southeast",
        "wealth":"east",
        "avoid":"northeast,west,southwest,northwest",
        "donate":"take blessings from seniors"
   }
}

dob = input("Enter your date of birth (dd/mm/yyyy): ")
gender = input("Enter your gender (male/female): ")
k = str(kua_number(dob, gender))

directions = kua_category_directions[k]

print("\nYour kua number is: ", k)
print("\ndirections based on your kua number:")
print("love direction: ",directions["love"])
print("growth direction: ",directions["growth"]) 
print("health direction: ",directions["health"])
print("wealth direction: ",directions["wealth"])
print("avoid directions: ",directions["avoid"])
print("donation suggestion: ",directions["donate"])

#calculate kua number
def kua_number(dob,gender):
    year=int(dob[-4:])
    total=sum(int(d) for d in str(year))

    while total > 9:
        total = sum(int(d) for d in str(total))

    if gender == "male":
        kua = 11 - total 
    else:
        kua = total + 4

        while kua > 9:
            kua = sum(int(d) for d in str(kua))
    return kua


    
  