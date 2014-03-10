#function hint

def print_greeting(number, name):
    print "Hello, I am number #{} my name is {}".format(number, name)


def main():
    my_names = ["sam", "barney", "joe"]
    for i, my_name in enumerate(my_names):
        print_greeting(i, my_name)

if __name__ == "__main__":
    main()

