import random
start = input('請輸入數字範圍的開始值：')
end = input('請輸入數字範圍的結束值：')
start = int(start)
end = int(end)
number = random.randint(start,end)
count = 0 #計次數
while True:
	count += 1 #count = count + 1
	n = input('猜數字：')
	n = int(n)
	if n == number:
		print('你終於猜對了！')
		print('這是你猜的第',count,'次')
		break #逃出迴圈
	elif n > number:
		print('再小一點喔！')
	elif n < number:
		print('再大一點喔！')
	print('這是你猜的第',count,'次')