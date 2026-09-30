import math

history = []

def calculator():
    while True:
        print("\n" + "="*40)
        print("   ADVANCED PYTHON CALCULATOR")
        print("=" * 40)
        
        
        print("""
1. addition(+)
2. subtraction(-)
3. multiplication(*)
4. division(/)
5. power(^)
6. square root(√)
7.percentage(%)
8.factorial(!)
9.sin
10.cos
11.tan
12.show history
13.exit
""")
        choice = input("enter your choice: ")
        
        #addition
        if choice == "1":
            a = float(input ("enter first number: "))
            b = float(input("enter second number: "))
            result = a+b
            print("result =",result)
            history.append(f"{a} + {b} = {result}")
            
            
        #subtraction
        elif choice == "2":
            a = float(input("enter first number: " ))
            b = float(input("enter second number: "))
            result = a-b
            print("result =", result)
            history.append(f"{a} - {b} = {result}")
            
                      
        #multiplication
        elif choice == "3":
            a = float(input("enter first number  : "))
            b = float(input("enterond number: "))
            result = a*b
            print("result =", result)
            history.append(f" {a} * {b} ={result}")
            
        #division   
        elif choice == "4":
            a = float(input("enter first number: "))
            b = float(input("enter second number: "))
            
            
            if b == 0:
                print("❌ cannot divide by zero!")
            else:
                result = a/b
                print("result = ", result)
                history.append(f"{a}/{b} ={result}")
                
                
        #power
        elif choice == "5":
            a =float(input("enter base: "))
            b = float(input("enter power: "))
            result = a**b
            print("result =", result)
            history.append(f"{a}^{b} ={result}")
            
        
        #square root
        elif choice == "6":
            a =float(input("enter number: "))
            
            
            if a<0:
                print("❌ square root of negative number is not possible.")
            else:
                result = math.squt(a)
                print("result =", result)
                history.appent(f"✓{a} ={result}")
                
                
                
        #percentage
        elif choice == "7":
            number = float(input("enter number : "))
            percent = float(input("enter percentage: "))
            
            
            
            result = (number * percent) / 100
            
            print(f"{percent}% of {number} = {result}")
            history.append (f"{percent}% of {number}={result}")
            
            
            
        #factorial
        elif choice == "8":
            a = int(input("enter a positive integer: "))
            
            
            if a<0:
                print("❌ factorial cannot be negative.")  
            else:
                result = math.factorial(a)  
                print("result =",result)
                history.append(f"{a}! = {result}") 
                
                
        #sin
        elif choice == "9":
            angle = float(input("enter angle in degrees:"))
            result = math.sin(math.radians(angle))
            
            
            print("result =", result)
            history.append(f"sin({angle}°) = {result}")

        
        #cos 
        elif choice == "10":
            angle = float(input("enter angle in degrees :"))
            result = math.cos(math.radians(angle))
            
            
            print("result =", result)
            history.append(f"cos({angle}°) = {result}")
            
            
            
        #tan
        elif choice == "11":
            angle = float(input("enter angle in degrees:"))
            result = math.tan(math.radians(angle))
            
            
            print("result =", result)
            history.append(f"tan({angle}°) = {result}") 
            
            
        #history
        elif choice == "12":
             print("\n------ CALCULATION HISTORY ------")

             if len(history) == 0:
                print("No calculations yet.")
             else:
                for i, calculation in enumerate(history, 1):
                    print(f"{i}. {calculation}")
                    
                    
        #exit
        elif choice == "13":
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")
            
            
            
calculator()