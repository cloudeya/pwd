password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwa = input('請輸入密碼')
	if password == pwa:
		print('登入成功')
		break
	elif i > 0:
		print('密碼錯誤,還有', i ,'次機會')
	else:
		print('沒機會了')
