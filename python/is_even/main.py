from is_even import is_even

while True:
    print("Imput an integer")
    try:
        num = int(input())
        if is_even(num):
            print("{} is even.".format(num))
        else:
            print("{} is odd.".format(num))

    except ValueError as e :
        print(e)
