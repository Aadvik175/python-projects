from operator import add,sub,mul,truediv,mod,floordiv
operation = {"+":add,"-":sub,"*":mul,"/":truediv,"%":mod,"//":floordiv}
num1 = float(input("Enter your number:"))

sign = str(input("Enter an operator(+,-,*,/,%,//):"))
num2 = float(input("Enter another number:"))

print(num1,sign, num2, "=", operation[sign](num1, num2))