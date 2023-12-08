    
print("\n\nCS112: COMPUTER PROGRAMMING 1 - PRE FINAL EXAM")
print("CREATED BY: Hally Marie D. Emano\n")   
print("PROBLEM: Create a python program that display all prime number within a range\n")
print("RULES TO CONSIDER:")
print("[1] If number[start] is a negative number, The program will promt a message: Enter a non-negative number.")
print("[2] If number[end] is less than number[start]. The program will promt a message: Enter a Greater number than number[start].")
print("[3] If the user enter the number 0, the program will terminate.\n\n\n")

while True:   
    first = int(input("\nEnter a number [start]: "))

    if first == 0:
        print("Program Terminated.")
        break
    
    if first < 0:
        print("Enter a non-negative number.")
        continue
    
    last = int(input("\nEnter a number [end]: "))
    
    if last <= first:
        print(f"Enter a number greater than {first}.")
        continue
    
    print(f"Prime numbers between {first} to {last} are: ", end=" ")
    
    for n in range(first, last + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                print(n, end=" ")
    
    print()