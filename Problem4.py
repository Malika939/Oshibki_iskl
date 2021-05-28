pay = float(input('Введите размер кредита ( > 50 000) -> '))
cred_proc = 3.47
ret_pay = pay * (1 + cred_proc/100)
print('Нужно вернуть {:.2f}'.format(round(ret_pay, 2)))