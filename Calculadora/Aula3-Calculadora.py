a=float(input("Digite o primeiro número: "))
c=input("Insira uma operação (*, +, /, -, ^, root, inv, sqr)").lower()
if c != "inv" and c != "sqr":
    b=float(input("Digite o segundo número: "))

if c == "*":
    print(a*b)
elif c == "+":
    print(a+b)
elif c == "/":
    print(a/b)
elif c == "-":
    print(a-b)
elif c == "^" or c == "**":
    print(a**b)
elif c == "root" or c == "r":
    print(a**(1/b))
elif c == "inv" or c == "i":
    print(1/a)
elif c == "sqr":
    print(a**2)
else:
    print("Operation not valid!")