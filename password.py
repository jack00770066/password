password = 'a123456'
typetimes = 0
chance = 3
while typetimes < 3:
	text = input('請輸入密碼:')
	if text != 'a123456':
		chance = chance - 1
		print('密碼錯誤!還有', chance, '次機會')
		typetimes += 1
		if chance == 0:
			print('錯誤次數過多，我們將鎖住您的帳號')
			break
	elif password == 'a123456':
		print('登入成功!')
		break