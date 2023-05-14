S_bin = set()  #Множество двоичных чисел
S_dec = set()   #Множество десятичных чисел

def convertation(S_bin):     #Функция для перевода в 10 сс
    for i in S_bin:
        S_dec.add(int(str(i), base=2))
    return S_dec


print("To finish typing, enter any character except 0 and 1.")
while (True):
    print("Write element in bin:")
    input_bin = str(input())
    for i in input_bin:
        if i != '0' and i != '1' and i:
            if S_bin != set():
                set_dec = convertation(S_bin)
                print("The set of binary numbers: \n", *S_bin)
                print("The set of decimal numbers: \n", *S_dec)
            exit()
    if int(input_bin) in S_bin:
        print("This element is already in the set. Try again.")
    else:
        S_bin.add(int(input_bin))