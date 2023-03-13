# from google.colab import output
# first functions are defined and then called

def menu():
    print("[+] - addition\n")
    print("[-] - subtraction\n")
    print("[*] - multiplication\n")
    print("[/] - division\n")

def calculator(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return('you have entered a wrong operator...')
    
# main code

while True:
    menu()
    a = int(input('1. number '))
    b = int(input("2. number "))
    op = input("enter a operator ")
    result = calculator(a,b,op)
    print("result is :", result)
    prompt = input('would you like to continue..')
    if prompt.lower() != "y" and prompt.lower != 'yes':
        print('finished!')
        break
 #  output.clear() it clears display