#check if a no is a perfect square



print('Enter a digit')
number = input()
flag=0
for i in range(1,number):
    if i*i==number:
        flag=1
        break
if flag==1:
    print('its a perfect square')
else:
    print('its not a perfect square')

