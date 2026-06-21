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
#output
print("\nName:", name)
print("Name Number:", total)
