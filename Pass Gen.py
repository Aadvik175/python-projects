import random as r
char = ("ABCDEFGHIJKLMNOPQRSTUVWRYZabcdefghijklmnopqrstuvwxyz0123456789)(*&^%$£?><,./[]{}#~+=_-|\¬`¦²³!Ç◙Ê■Ý♫Ä♠áàç▼↨♪ëÎ┘↔ùñÆ┤ãê╩L§♣╚╔╩╦╠═╬®☺☻♥♦•◘○◙♂♀☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ ¹■ +½Ì«╬µ▀╔°Ó‗©÷†ƒ×ž‘¥‰±¨Œªø™‡ÔÙÚÛÜÒßÞÿ┐¿")
print("The max length for the password is",len(char))
pass_len = int(input("Enter a length for a password:"))
passw = "".join(r.sample(char,pass_len))
print(passw)