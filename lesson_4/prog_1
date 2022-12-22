import sys
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default="10")

    return parser

def fib(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])


    if namespace.name:
        answer = fib(namespace.name)
        print(f"the number is {answer}")
    else:
        print("error, you've entered the wrong way")
