#chaldean numerology
CHART={
 'A':1,'I':1,'J':1,'Q':1,'Y':1,
 'B':2,'K':2,'R':2,
 'C':3,'G':3,'L':3,'S':3,
 'D':4,'M':4,'T':4,
 'E':5,'H':5,'N':5,'X':5,
 'U':6,'V':6,'W':6,
 'O':7,'Z':7,
 'F':8,'P':8,
 }
def reduce_number(n):
    while n>9:
        n=sum(int(i) for i in str(n))
    return n

def name_number(name):
    total=0
    for char in name.upper():
        if char in CHART:
            total+=CHART[char]
    return reduce_number(total)

#input
name=input("Enter a name: ")
#calculation
total,final_number=name_number(name),reduce_number(name_number(name))


#calculate kua number
def kua_number(dob,gender):
    year=int(dob.split('/')[-1])  # Extract the year from the DOB
    last_two_digits = year % 100  # Get the last two digits of the year
    total=sum(int(d) for d in str(last_two_digits))  # Sum the digits of the last two digits
    #reduce to a single digit


    while total > 9:
        total = sum(int(d) for d in str(total))

    if gender.lower() == "male":
        kua = 11 - total 
    else:
        kua = total + 4

        while kua > 9:
            kua = sum(int(d) for d in str(kua))
            if kua == 0:
                kua = 1
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
#numerology data
numerology_analysis = {
1:{"lucky numbers":[2,3,5,9],"unlucky numbers":[8],"lucky colors":["all shades of sun"],"unlucky colors":["black"],"element":["water"],"direction":["north"],"missing number effects":"cannot express feelings,dependent,less focused","missing number remedy":"keep water fountain in north direction/hang a painting of flowing water in north direction/hang a mirrorof 9 inch by 9 inch in north direction/take blessings from father","repeating number more than one time effects":"becomes introvert,talkactive,over emotional","repeating number more than one time remedy":"offer water to sun/keep north direction clean/keep orange cloth with 2 wheat/wear copper/donate red color things on sunday"},

2:{"lucky numbers":[1,3,5],"unlucky numbers":[4,6,7,8],"lucky colors":["white,silver"],"unlucky colors":["red,black"],"element":["earth"],"direction":["southwest"],"missing number effects":"gets irritated easily,relationship issues","missing number remedy":"hang a painting of moutain without water in southwest direction/offer milk on shivling/take blessings from mother","repeating number more than one time effects":"sensitive","repeating number more than one time remedy":"stay in moonlight/donate any white color things on monday example water,milk,rice,etc/keep 27 rice in white cloth"},

3:{"lucky numbers":[1,2,7,9],"unlucky numbers":[6],"lucky colors":["yellow,red,orange"],"unlucky colors":["white"],"element":["wood"],"direction":["east"],"missing number effects":"lack of confidence,not logical,unstable career","repeating number more than one time remedy":"east direction should be clean/respect to elders and teachers,plant turmeric tree/donate yellow color things every thursday/keep 3 chana daal in yellow cloth","repeating number more than one time effects":"delusional","missing number remedy":"keep plant in east dirstion/keep yellow bulb in east direction/wear yellow band in right hand/keep wooden pen or keychain with you/hang wooden wallclock in octagon shape in east direction/respect gurus"},

4:{"lucky numbers":[1,3,5,7],"unlucky numbers":[2,4,8,9],"lucky colors":["blue"],"unlucky colors":["red","black"],"element":["wood"],"direction":["southeast"],"missing number effects":"lack of discipline,motivation,cannot save money","missing number remedies":"plant a tree in southeast direction/keep energized green pyramid in southeast direction/wear tulsi mala/hang wooden windchime in southeast direction","repeating number more than one time effects":"hardworking","repeating number more than one time remedy":"keep 4 jowar in black/brown cloth/donate electric things"},

5:{"lucky numbers":[1,3,5,6,7,9],"unlucky numbers":[4,6,8],"lucky colors":["green"],"unlucky colors":["black"],"element":["earth"],"direction":["center"],"missing number effects":"lack of strength,stability,upset stomach","missing number remedy":"keep green handkerchief,use green color pen,keep crystal in center","repeating number more than one time effects":"stomach problems","repeating number more than one time remedy":"donate green color things on wednesday/keep cardom in green cloth"},

6:{"lucky numbers":[1,5,6,7,8],"unlucky numbers":[2,3,9],"lucky colors":["white"],"unlucky colors":["yellow"],"element":["metal"],"dirction":["northwest"],"missing number effects":"lack in luxury,problem with partner,less support from friends","missing number remedy":"wear golden metallic watch/hang golden 6 rod windchime/keep white handkerchief/keep pair of elephant in northwest direction","repeating number more than one time effects":"skin disease","repeating number more than one time remedy":"donate white color things on friday"},

7:{"lucky numbers":[4,5,7,8],"unlucky numbers":[2,6,9],"lucky colors":["light colors"],"unlucky colors":["dark colors"],"element":["metal"],"direction":["west"],"missing number effects":"less chance of first male child,less support from family,not interest in spirtuality","missing number remedy":"wear silver metallic watch/hang 7 silver metallic rod windchime/feed black dog/wear a white silver armlet","repeating number more than one time effects":"slow learner","repeating number more than one time remedy":"keep 7 black seed in white or black cloth"},

8:{"lucky numbers":[3,5,6,7,8],"unlucky numbers":[1,2,4,9],"lucky colors":["dark blue"],"unlucky colors":["black","red"],"element":["earth"],"direction":["northeast"],"missing number effects":"careless,trust easily,poor in handling financial matters","missing number remedy":"keep gangajal in northeast direction,place om in golden frame in northeast direction","repeating number more than one time effects":"materalistic","repeating number more than one time remedy":"donate black color things on saturday/keep 8 black pepper in black cloth"},

9:{"lucky numbers":[1,3,5,6,7],"unlucky numbers":[2,4,8],"lucky colors":["red"],"unlucky colors":["light colors"],"element":["fire"],"direction":["south"],"missing number effects":"no fame,detachment","missing number remedy":"put red bulb in south direction,keep red pyramid in south direction ","repeating number more than one time effects":"short tempered","repeating number more than one time remedy":"donate red color things on tuesday/keep 9 masoor daal in red cloth"}
}


#mulank
def bhagyank(dob):
    total=sum(int(d) for d in dob if d.isdigit())
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total
#bhagyank
def mulank(dob):
    day=int(dob[:2])
    while day > 9:
        day = sum(int(d) for d in str(day))
    return day
#missing and repeating numbers
def analyze_numbers(dob):
    # Remove non-numeric characters (like / or -)
    dob_digits = [int(d) for d in dob if d.isdigit()]
    
    # Count frequency of each number
    count = {}
    for num in dob_digits:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Find missing/repeating numbers


def numerology_analysis(dob, mulank, bhagyank, name_number, kua_number):
    # Convert DOB to string and extract digits
    dob_str = str(dob)
    digits = [int(d) for d in dob_str if d.isdigit() and d != '0']
    
    # Count frequency of each number
    freq = {}
    for d in digits:
        freq[d] = freq.get(d, 0) + 1

    # Repeating numbers (more than 1 time)
    repeating_numbers = [num for num, count in freq.items() if count > 1]

    # Numbers present in other numerology values
    extra_numbers = set()
    for value in [mulank, bhagyank, name_number, kua_number]:
        for digit in str(value):
            if digit != '0':
                extra_numbers.add(int(digit))

    # Missing numbers (1–9 not in DOB AND not in other values)
    missing_numbers = []
    for i in range(1, 10):
        if i not in digits and i not in extra_numbers:
            missing_numbers.append(i)
    return {
        "missing_numbers": missing_numbers,
        "repeating_numbers": repeating_numbers
    }

    



    

    
    


    
    



#input
dob = input("Enter your date of birth (dd/mm/yyyy): ")
gender = input("Enter your gender (male/female): ")
#calculations
total,final_number=name_number(name),reduce_number(name_number(name))
mulank_value=mulank(dob)
bhagyank_value=bhagyank(dob)
k = str(kua_number(dob, gender))
missing_repeating_result = numerology_analysis(dob, mulank_value, bhagyank_value, total, int(k))
missing_numbers=missing_repeating_result["missing_numbers"]        
repeating_numbers=missing_repeating_result["repeating_numbers"]




k = str(kua_number(dob, gender))
directions = kua_category_directions[k]


#output
print("\nName:", name)
print("Name Number:", total)
print("Mulank:", mulank_value)
print("Bhagyank:", bhagyank_value)
print("Missing Numbers:", missing_repeating_result["missing_numbers"])
print("Repeating Numbers:", missing_repeating_result["repeating_numbers"])
print("\nYour kua number is: ", k)
print("\ndirections based on your kua number:")
print("love direction: ",directions["love"])
print("growth direction: ",directions["growth"])
print("health direction: ",directions["health"])
print("wealth direction: ",directions["wealth"])
print("avoid directions: ",directions["avoid"])
print("donation suggestion: ",directions["donate"])
print("\nnumerology analysis:")

    
if mulank_value == 1:
    lucky_numbers = [2,3,5,9]
    unlucky_numbers = [8]
    lucky_colors = ["all shades of sun"]
    unlucky_colors = ["black"]
    element = "water"
    direction = "north"
   
elif mulank_value == 2:
    lucky_numbers = [1,3,5]
    unlucky_numbers = [4,6,7,8]
    lucky_colors = ["white,silver"]
    unlucky_colors = ["red,black"]
    element = "earth"
    direction = "southwest"
    
elif mulank_value == 3:
    lucky_numbers = [1,2,7,9]
    unlucky_numbers = [6]
    lucky_colors = ["yellow,red,orange"]
    unlucky_colors = ["white"]
    element = "wood"
    direction = "east"
    
elif mulank_value == 4:
    lucky_numbers = [1,3,5,7]
    unlucky_numbers = [2,4,8,9]
    lucky_colors = ["blue"]
    unlucky_colors = ["red","black"]
    element = "wood"
    direction = "southeast"
    
elif mulank_value == 5:
    lucky_numbers = [1,3,5,6,7,9]
    unlucky_numbers = [4,6,8]
    lucky_colors = ["green"]
    unlucky_colors = ["black"]
    element = "earth"
    direction = "center"
    
elif mulank_value == 6:
    lucky_numbers = [1,5,6,7,8]
    unlucky_numbers = [2,3,9]
    lucky_colors = ["white"]
    unlucky_colors = ["yellow"]
    element = "metal"
    direction = "northwest"
   
elif mulank_value == 7:
    lucky_numbers = [4,5,7,8]
    unlucky_numbers = [2,6,9]
    lucky_colors = ["light colors"]
    unlucky_colors = ["dark colors"]
    element = "metal"
    direction = "west"
    
elif mulank_value == 8:
    lucky_numbers = [3,5,6,7,8]
    unlucky_numbers = [1,2,4,9]
    lucky_colors = ["dark blue"]
    unlucky_colors = ["black","red"]
    element = "earth"
    direction = "northeast"
   
elif mulank_value == 9:
    lucky_numbers = [1,3,5,6,7]
    unlucky_numbers = [2,4,8]
    lucky_colors = ["red"]
    unlucky_colors = ["light colors"]
    element = "fire"
    direction = "south"
    
print("lucky numbers:",lucky_numbers)
print("unlucky numbers:",unlucky_numbers)   
print("lucky colors:",lucky_colors)
print("unlucky colors:",unlucky_colors)
print("element:",element)
print("direction:",direction)

if bhagyank_value == 1:
    print("\nBhagyank is 1, which means you are a natural leader with a strong sense of independence. You have a creative and innovative mind, and you are not afraid to take risks. You are ambitious and have the potential for great success in life. However, you may also be prone to stubbornness and may need to work on being more flexible in your approach to life.") 
elif bhagyank_value == 2:
    print("\nBhagyank is 2, which means you are a peacemaker and a diplomat. You have a strong sense of empathy and are able to understand the feelings of others. You are cooperative and work well in teams, and you have a natural talent for bringing people together. However, you may also be prone to indecisiveness and may need to work on being more assertive in your decisions.")
elif bhagyank_value == 3:
    print("\nBhagyank is 3, which means you are a creative and expressive individual. You have a natural talent for communication and are able to express yourself in a unique and artistic way. You are optimistic and have a positive outlook on life, and you have the potential for great success in creative fields. However, you may also be prone to being scattered and may need to work on staying focused on your goals.")
elif bhagyank_value == 4:
    print("\nBhagyank is 4, which means you are a practical and hardworking individual. You have a strong sense of responsibility and are able to create a solid foundation for yourself and those around you. You are organized and detail-oriented, and you have the potential for great success in fields that require precision and attention to detail. However, you may also be prone to being rigid and may need to work on being more adaptable in your approach to life.")
elif bhagyank_value == 5:
    print("\nBhagyank is 5, which means you are a free spirit with a love for adventure and new experiences. You have a natural talent for communication and are able to connect with people from all walks of life. You are adaptable and thrive in dynamic environments, and you have the potential for great success in fields that require creativity and innovation. However, you may also be prone to being restless and may need to work on finding stability in your life.")
elif bhagyank_value == 6:
    print("\nBhagyank is 6, which means you are a nurturing and caring individual. You have a strong sense of responsibility and are able to create a harmonious environment for yourself and those around you. You are compassionate and have a natural talent for helping others, and you have the potential for great success in fields that require empathy and understanding. However, you may also be prone to being overly self-sacrificing and may need to work on setting healthy boundaries in your relationships.")
elif bhagyank_value == 7:
    print("\nBhagyank is 7, which means you are a deep thinker with a strong sense of intuition. You have a natural talent for analysis and are able to see things from a unique perspective. You are introspective and have a love for knowledge, and you have the potential for great success in fields that require research and analysis. However, you may also be prone to being aloof and may need to work on connecting with others on a deeper level.")
elif bhagyank_value == 8:
    print("\nBhagyank is 8, which means you are a powerful and ambitious individual. You have a natural talent for leadership and are able to achieve great success in your career. You are confident and have a strong sense of self-worth, and you have the potential for great financial success. However, you may also be prone to being materialistic and may need to work on finding balance in your life.")
elif bhagyank_value == 9:
    print("\nBhagyank is 9, which means you are a compassionate and humanitarian individual. You have a strong sense of empathy and are able to understand the feelings of others. You are idealistic and have a love for helping others, and you have the potential for great success in fields that require compassion and understanding. However, you may also be prone to being overly emotional and may need to work on finding balance in your emotions.")

if bhagyank_value == 1:
    lucky_numbers = [2,3,5,9]
    unlucky_numbers = [8]
    lucky_colors = ["all shades of sun"]
    unlucky_colors = ["black"]
    element = "water"
    direction = "north"
   
elif bhagyank_value == 2:
    lucky_numbers = [1,3,5]
    unlucky_numbers = [4,6,7,8]
    lucky_colors = ["white,silver"]
    unlucky_colors = ["red,black"]
    element = "earth"
    direction = "southwest"
    
elif bhagyank_value == 3:
    lucky_numbers = [1,2,7,9]
    unlucky_numbers = [6]
    lucky_colors = ["yellow,red,orange"]
    unlucky_colors = ["white"]
    element = "wood"
    direction = "east"
    
elif bhagyank_value == 4:
    lucky_numbers = [1,3,5,7]
    unlucky_numbers = [2,4,8,9]
    lucky_colors = ["blue"]
    unlucky_colors = ["red","black"]
    element = "wood"
    direction = "southeast"
   
elif bhagyank_value == 5:
    lucky_numbers = [1,3,5,6,7,9]
    unlucky_numbers = [4,6,8]
    lucky_colors = ["green"]
    unlucky_colors = ["black"]
    element = "earth"
    direction = "center"
    
elif bhagyank_value == 6:
    lucky_numbers = [1,5,6,7,8]
    unlucky_numbers = [2,3,9]
    lucky_colors = ["white"]
    unlucky_colors = ["yellow"]
    element = "metal"
    direction = "northwest"
   
elif bhagyank_value == 7:
    lucky_numbers = [4,5,7,8]
    unlucky_numbers = [2,6,9]
    lucky_colors = ["light colors"]
    unlucky_colors = ["dark colors"]
    element = "metal"
    direction = "west"
    
elif bhagyank_value == 8:
    lucky_numbers = [3,5,6,7,8]
    unlucky_numbers = [1,2,4,9]
    lucky_colors = ["dark blue"]
    unlucky_colors = ["black","red"]
    element = "earth"
    direction = "northeast"
    
elif bhagyank_value == 9:
    lucky_numbers = [1,3,5,6,7]
    unlucky_numbers = [2,4,8]
    lucky_colors = ["red"]
    unlucky_colors = ["light colors"]
    element = "fire"
    direction = "south"
    
print("lucky numbers:",lucky_numbers)
print("unlucky numbers:",unlucky_numbers)
print("lucky colors:",lucky_colors)
print("unlucky colors:",unlucky_colors)
print("element:",element)
print("direction:",direction)

for num in missing_numbers:

 if num  == 1:
    print("\nSince you have missing number 1, you may find it difficult to express your feelings and may be dependent on others. You may also struggle with focus and concentration. To remedy this, you can keep a water fountain in the north direction of your home, hang a painting of flowing water in the north direction, or hang a mirror of 9 inch by 9 inch in the north direction. Additionally, taking blessings from your father can also help.")
    missing_number_remedy = "keep water fountain in north direction/hang a painting of flowing water in north direction/hang a mirrorof 9 inch by 9 inch in north direction/take blessings from father"
 elif num == 2 :
    print("\nSince you have missing number 2, you may find yourself getting irritated easily and may experience relationship issues. To remedy this, you can hang a painting of a mountain without water in the southwest direction of your home, offer milk on a shivling, or take blessings from your mother.")
    missing_number_remedy = "hang a painting of moutain without water in southwest direction/offer milk on shivling/take blessings from mother"
 elif num == 3:
    print("\nSince you have missing number 3, you may struggle with confidence, logic, and may have an unstable career. To remedy this, you can keep a plant in the east direction of your home, keep a yellow bulb in the east direction, wear a yellow band on your right hand, keep a wooden pen or keychain with you, hang a wooden wall clock in octagon shape in the east direction, and respect gurus.")
    missing_number_remedy = "keep plant in east dirstion/keep yellow bulb in east direction/wear yellow band in right hand/keep wooden pen or keychain with you/hang wooden wallclock in octagon shape in east direction/respect gurus"
 elif num == 4:
    print("\nSince you have missing number 4, you may struggle with discipline, motivation, and may find it difficult to save money. To remedy this, you can plant a tree in the southeast direction of your home, keep an energized green pyramid in the southeast direction, wear a tulsi mala, and hang a wooden wind chime in the southeast direction.")
    missing_number_remedy = "plant a tree in southeast direction/keep energized green pyramid in southeast direction/wear tulsi mala/hang wooden windchime in southeast direction"
 elif num == 5:
    print("\nSince you have missing number 5, you may struggle with strength, stability, and may experience an upset stomach. To remedy this, you can keep a green handkerchief, use a green color pen, and keep a crystal in the center of your home.")
    missing_number_remedy = "keep green handkerchief,use green color pen,keep crystal in center"
 elif num == 6:
    print("\nSince you have missing number 6, you may struggle with luxury, have problems with your partner, and may receive less support from friends. To remedy this, you can wear a golden metallic watch, hang a golden 6 rod wind chime, keep a white handkerchief, and keep a pair of elephants in the northwest direction of your home.")
    missing_number_remedy = "wear golden metallic watch/hang golden 6 rod windchime/keep white handkerchief/keep pair of elephant in northwest direction"
 elif num == 7:
    print("\nSince you have missing number 7, you may find that you have less chance of success. To remedy this, you can keep a white handkerchief and keep a pair of elephants in the west direction of your home.")
    missing_number_remedy = "keep white handkerchief/keep pair of elephant in west direction"
 elif num == 8:
    print("\nSince you have missing number 8, you may find that you are careless, trust easily, and may be poor in handling financial matters. To remedy this, you can keep gangajal in the northeast direction of your home and place an om in a golden frame in the northeast direction.")
    missing_number_remedy = "keep gangajal in northeast direction,place om in golden frame in northeast direction"
 elif num == 9:
    print("\nSince you have missing number 9, you may find that you have no fame and may experience detachment. To remedy this, you can put a red bulb in the south direction of your home and keep a red pyramid in the south direction.")
    missing_number_remedy = "put red bulb in south direction,keep red pyramid in south direction "
 for num in repeating_numbers:
    
    if num == 1:
        print("\nSince you have repeating number 1, you may find that you become introverted, talkative, and over emotional. To remedy this, you can offer water to the sun, keep the north direction of your home clean, keep an orange cloth with 2 wheat in the north direction, wear copper jewelry, and donate red color things on Sunday.")
        repeating_number_remedy = "offer water to sun/keep north direction clean/keep orange cloth with 2 wheat/wear copper/donate red color things on sunday"
    elif num == 2:
        print("\nSince you have repeating number 2, you may find that you are sensitive. To remedy this, you can stay in moonlight, donate any white color things on Monday (such as water, milk, rice, etc.), and keep 27 rice grains in a white cloth.")
        repeating_number_remedy = "stay in moonlight/donate any white color things on monday example water,milk,rice,etc/keep 27 rice in white cloth"
    elif num == 3:
        print("\nSince you have repeating number 3, you may find that you are delusional. To remedy this, you can keep the east direction of your home clean, show respect to elders and teachers, plant a turmeric tree, donate yellow color things every Thursday, and keep 3 chana daal in a yellow cloth.")
        repeating_number_remedy = "east direction should be clean/respect to elders and teachers,plant turmeric tree/donate yellow color things every thursday/keep 3 chana daal in yellow cloth"
    elif num == 4:
        print("\nSince you have repeating number 4, you may find that you are hardworking. To remedy this, you can keep 4 jowar grains in a black or brown cloth and donate electric things.")
        repeating_number_remedy = "keep 4 jowar in black/brown cloth/donate electric things"
    elif num == 5:
        print("\nSince you have repeating number 5, you may find that you have stomach problems. To remedy this, you can donate green color things on Wednesday and keep cardamom in a green cloth.")
        repeating_number_remedy = "donate green color things on wednesday/keep cardom in green cloth"
    elif num == 6:
        print("\nSince you have repeating number 6, you may find that you have skin diseases. To remedy this, you can donate white color things on Friday.")
        repeating_number_remedy = "donate white color things on friday"
    elif num == 7:
        print("\nSince you have repeating number 7, you may find that you are a slow learner. To remedy this, you can keep 7 black seeds in a white or black cloth.")
        repeating_number_remedy = "keep 7 black seed in white or black cloth"
    elif num == 8:
        print("\nSince you have repeating number 8, you may find that you are materialistic. To remedy this, you can donate black color things on Saturday and keep 8 black pepper grains in a black cloth.")
        repeating_number_remedy = "donate black color things on saturday/keep 8 black pepper in black cloth"
    elif num == 9:
        print("\nSince you have repeating number 9, you may find that you are short tempered. To remedy this, you can donate red color things on Tuesday and keep 9 masoor daal in a red cloth.")
        repeating_number_remedy = "donate red color things on tuesday/keep 9 masoor daal in red cloth"
    
    
print("Based on your numerology analysis, it is important to focus on the remedies suggested for your missing and repeating numbers. By following these remedies, you can work towards improving the areas of your life that may be affected by these numbers. Remember to stay positive and open to change as you implement these remedies into your daily routine.")    
print("for more personalized guidance, consider consulting with a professional numerologist who can provide deeper insights into your unique numerology chart and offer tailored advice for your specific circumstances. ")
print("vrushali shinde contact: 8104594224")