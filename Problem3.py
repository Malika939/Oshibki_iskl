w = ["all","any","abs","min","eval","reversed","max","slice","round"]
d = input("напиши функцию: ")
i=0
try:
    while w[i] != d:
        print("не правильно")
        i+=10
    else:
        print(d, "правильно")
except IndexError:
    print("у вас не правильно")