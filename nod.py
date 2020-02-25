a = abs(int(input("1 число: ")))
b = abs(int(input("2 число: ")))

if a < b:
    a, b = b, a

def get_result(a, b):
    mnog=0
    last_ost=0
    ost=1
    
    while (ost!=0):
        mnog = a//b
        last_ost = ost
        ost = a%b
        print("{} = {}*{}+{}".format(a, b, mnog, ost))
        a = b
        b = ost
    
    print("НОД: +-{}".format(last_ost))

if a == 0:
    print("НОД 0")
if b == 0:
    print("НОД = +-{}".format(a+b))
else:
    get_result(a,b)
