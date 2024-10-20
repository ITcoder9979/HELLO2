# Triangle Area Calculator
11
def area_triangle(h,b):
    a=h*b*0.5
    return a


   
def main():
    try:
        print("\n\n ::- _ TRIANGLES AREA CALCULATOR _ -::\n")        
        hieght=int(input("Enter the hieght of triangle. \n -> "))
        base=int(input("Enter length of base of triangle. \n-> "))
        unit=input(('Length given above are in which unit \n->'))
        area=area_triangle(hieght,base)
        print(area,"sq.",unit)
        
    except:
        print("pls input digts only\n -- try again --\n")
        main()

def choice():
    try:
        opt=int(input("\n:-:-:-:\nEnter 1 to find area ,2 to exit the code -\n ->  "))
        if opt==1:
            main()
        elif opt==2:
            return False
        elif opt<1 or opt>2:
            print("::  Wrong input ::\n Answer in 1 or 2 only \n -- try again --")
            choice()
        
    except:
        print("Give response in digits only\n -- try again --")
        choice()
while True:
    if choice()== False:
        break