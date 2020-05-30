import random
number = random.randint(1,100)
while True:
	n = input('猜數字：')
	n = int(n)
	if n == number:
		print('你終於猜對了！')
		break #逃出迴圈
	elif n > number:
		print('再小一點喔！')
	else:
		print('再大一點喔！')