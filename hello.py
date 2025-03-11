def square(z):
  print("{} 的平方{},三次方是{}".format(z,z*z,z**3)) 

x = int(input("請輸入一個正整數:"))
print("您輸入的數字是",x)

if(x<0):
	print("您輸入的值為負數")
elif(x==0):
	print("您輸入的值小於等於0")
else:
	for i in range(1,x+1):
		square(i)


