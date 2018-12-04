password = 'a123456'
typetimes = 0
chance = 3
while typetimes < 3:
	text = input('請輸入密碼:')
	if text != password:
		chance = chance - 1
		if chance == 0:
			print('你沒機會了，錯誤次數過多，我們將鎖住您的帳號')
			break
		else:
			print('密碼錯誤!還有', chance, '次機會')
			typetimes += 1
	elif text == password:
		print('登入成功!')
		break