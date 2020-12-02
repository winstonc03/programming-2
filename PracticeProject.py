# PracticeProject.py

# Code to practice using Git

def main():
    """"" Calculate the nth Fibonacci number"""
    # 1, 1, 2, 3, 5, 8, ...

    # Ask user which fib number they want
    num = int (input("Which Fibonacci number do you want?"))

    # start at n = 1 -> 1
    #          n = 2 -> 1
    #          n = 3 -> 2
    if num == 1 or  num == 2:
        print(f"The {num}st/nd Fibonacci number is 1")


if __name__ == "__main__":
    main()

