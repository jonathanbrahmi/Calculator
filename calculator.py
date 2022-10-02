#This programe written by Jonathan brahmi


def minus():
    print("-------------------------------------------\n")
    print("        ====Subtraction====\n")
    x = int(input("Please put here an digit>>"))
    y = int(input("Please put here an digit again>>"))
    sum = x - y
    print("result => " + str(sum) + "\n")
    print("-------------------------------------------\n")


def plus():
    print("-------------------------------------------\n")
    print("          ====Addition====\n")
    x = int(input("Please put here an digit>>"))
    y = int(input("Please put here an digit again>>"))
    sum = x + y
    print("result => " + str(sum) + "\n")
    print("------------------------------------------\n")

def double():
    print("------------------------------------------\n")
    print("         ====Multipaction====\n")
    x = int(input("Please put here an digit>>"))
    y = int(input("please put here an digit again>>"))
    sum = x * y
    print("result => " + str(sum) + "\n")
    print("------------------------------------------\n")


def main():
    print("Calculator v1.0.0 by Jonathan brahmi\n")
    print("*Warning the container sometimes doesn't work in the first time\ntry again if it doesn't start any function")
    print("functions menu")
    print("----")
    print("1> Subtraction")
    print("2> addition")
    print("3> multipaction\n")
    op = input("Choose any function and put here [1/2/3]>>")
    if op == '1':
       minus()
    elif op == '2':
       plus()
    elif op == '3':
       double()
    else:
       print(")-: ooops!!! this function is missing\n")
       print(".done")


main()






