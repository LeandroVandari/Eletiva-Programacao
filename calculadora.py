first_num = float(input("Select the first number: "))
operation = input("Select an operation (*, +, -, /): ")
second_num = float(input("Select the second number: "))
all_ops = ["*", "/", "+", "-"]
if operation in all_ops:
    print(eval(str(first_num) + operation + str(second_num)))
else:
    print("You didn't select a valid operation!")