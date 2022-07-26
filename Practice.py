a = input("Enter a number: \n")
a = int(a)
b = input("Enter another number: \n")
b = int(b)
list_c = ["margo","180th","184th","192nd"]
count_c = len(list_c)

def func1(a,b):
    while a < b:
        print(f"loop#{a}")
        if(a < count_c):
            print(list_c[a])
        a = a + 1
    print("Loop ended!!!")

<<<<<<< HEAD
#call function func1
=======
#call function
>>>>>>> subproject
func1(a,b)


