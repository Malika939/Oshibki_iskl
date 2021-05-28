values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
a = []
for i in values:
	try :
		set(i)
		a.append(True)
	except TypeError:
		a.append(False)
print(a)		
print(all(a))