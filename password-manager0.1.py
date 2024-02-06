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
names_passwords = []
print("Here your passwords:",p)

add_name = input("Add an names to passwords?(y/n)")
if add_name.lower() == 'y':
    for n in p:
        print("Add a name to ","'",n,"'",":",sep='')
        name = input("")
        names_passwords.append(name+':'+n)
    for n in names_passwords:
        print(n)
write_answ = input("Write passwords to file?(y/n)")

if write_answ.lower() == 'y' and add_name.lower() == 'n':
    file_name = input("Enter the file name to write passwords:")
    file_passw = open(file_name,'a')
    for i in p:
        file_passw.write(i+'\n')
    file_passw.close
if write_answ.lower() == 'y' and add_name.lower() == 'y':
    file_name = input("Enter the file name to write passwords:")
    file_passw = open(file_name,'a')
    for i in names_passwords:
        file_passw.write(i+'\n')
    file_passw.close
