Name = "Rishu"

def fn():
    print("What is your name")
    print("My name is", Name)
    rtn_val = "I got this!"
    return rtn_val


rtn_val = fn()
print("My name stays same bcause i am global variable", Name)
print("The return value is" , rtn_val)
