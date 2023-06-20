def my_func(func):
    def inner(name):
        if name == "sunny":
            print("hello sunny badmrng!!!")
        else:
            func(name)
    return inner
#@my_func
def wish(name):
    print("hello",name,"gudmrng!!!")

wish("raghava")
wish("sunny")
dec=my_func(wish)
dec("raghava")
dec("sunny")
dec("kiarn")


def smart_division(func):
    def inner(a,b):
        if b==0:
            print("we can;t divide if b is zero")
            return
        else:
            func(a,b)
    return inner
@smart_division

def division(a,b):
    return a/b

s=division(20,10)
print(s)

s=division(20,0)
print(s)


def wish(name):
    print("hi",name,"gudmrng!!")

wish("raghava")
wish("kiran")


def my_func(func):
    def inner(name):
        if name == "sunny":
            print("hello sunny badmrng!!!")
        else:
            func(name)
    return inner
#@my_func
def wish(name):
    print("hello",name,"gudmrng!!!")

wish("raghava")
wish("sunny")
dec=my_func(wish)
dec("raghava")
dec("sunny")
dec("kiarn")
