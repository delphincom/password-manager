from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
pass_num = int(input("Enter a number of passwords:"))
pass_len = int(input("Enter a length of passwords:"))
digits_answ = input('Include numbers?(y/n)')
upp_lett_answ = input('Include uppercase letters?(y/n)')
low_lett_answ = input('Include lowercase letters?(y/n)')
punct_answ = input('Include special symbols?(y/n)')
exceptions = input("Exclude monosemantic symbols 'il1Lo0O' ?(y/n)")
if digits_answ.lower() == 'y':
    chars+=digits
if upp_lett_answ.lower() == 'y':
    chars+=uppercase_letters
if low_lett_answ.lower() == 'y':
    chars+=lowercase_letters
if punct_answ.lower() == 'y':
    chars+=punctuation
if exceptions == "y":
    chars.replace('1','')
    chars.replace('0','')
    chars.replace('i','')
    chars.replace('I','')
    chars.replace('o','')
    chars.replace('l','')
    chars.replace('O','')
def pass_gen(length,chr):
     
    pass_lst = []
    for i in range(pass_num):
        s=''
        passw = sample(chr,length)
        for j in passw:
            s+=j
        pass_lst.append(s)
    return pass_lst
p = pass_gen(pass_len,chars)
print(p)
write_answ = input("Write passwords to file?(y/n)")
file_name = input("Enter the file name to write:")
if write_answ.lower() == 'y':
    file_passw = open(file_name,'a')
    for i in p:
        file_passw.write(' '+i+' ,')
    file_passw.close

