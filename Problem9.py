dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
try:
    for x in dict_.keys():
        x + 'abc'
except IndentationError:
    print("у вас ошибка")
except TypeError:
    print("у вас ошибка")
finally:
    print("у вас ошибка")