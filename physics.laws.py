import math 
import time
def packing_factor_for_cubic_system():
    type=input("Enter the type of cubic system :\n1.simple\n2.body centered\n3.face centered\n").lower()
    try:
        radius = float(input("Enter the radius in Angstrom: "))
        if radius <=0:
            print("Radius must be positive")
            return
        p = math.pi
        if type in ["1","simple"]:
            atom=1
            a= 2*radius
            pf= atom*(4/3 * p * radius**3) / (a**3)
            print("packing factor is",pf)
        elif type in ["2","body centered","body"]:
            atom=2
            a= ((4*radius)/math.sqrt(3)) 
            pf= (atom*(4/3*p*radius**3)/(a**3))
            print("packing factor is ",pf)
        elif type in ["3","face centered","face"]:
            atom=4
            a=((4*radius)/math.sqrt(2))
            pf= (atom*(4/3*p*radius**3)/(a**3))
            print("packing factor is ",pf)
        else:
            print("please Enter on of these: \n1.simple\n2.body centered\n3.face centered\n")
    except ValueError as e:
        print("Invalid input,please enter a number")     
def thermistor_law():
    type=input("Enter the type of thermistor:\n 1.NTC \n 2.PTC\n").lower()
    T=60+273
    try:
        if type in ["1","ntc"]:
            slope=float(input("Enter the slope in kelvin−1:"))
            alpha=-slope/(T**2)
            print("alpha is:",alpha)
        elif type in ["2","ptc"]:
            slope=float(input("Enter the slope:"))
            alpha=slope/(T**2)
            print("alpha is:",alpha)
        else:
            print("please enter the right type")
    except ValueError as e:
        print(e)
def melting_point_law():
    t_c=25
    T = (t_c+273)**4
    r=0.03
    Σ=0.3
    σ=5.67*10**-8
    p=math.pi
    while True:
        change=input(f"Do you wanna change any of these constants?\n1.raduis={r}mm\n2.temp={t_c}c\n3.Σ={Σ}\n4.σ={σ}\nYes or No?\n").lower()
        if change=="yes":
            while True:
                choice=input(f"Enter the constant you wanna change:\n1.raduis={r}\n2.temprature in celsius={t_c}\n3.Σ={Σ}\n4.σ={σ}\n5.stop\n").lower()
                if choice in["1","raduis","r"]:
                    r=float(input("Enter new raduis in mm:"))
                    if r<=0:
                        print("raduis must be positive")
                        return
                elif choice in ["2","temp","temprature","t","temprature in celsius"]:
                    t_c=float(input("Enter new temperature in celsius:"))
                elif choice in ["3","Σ","sigma"]:
                    Σ=float(input("Enter new Σ:"))
                elif choice in ["4","σ"]:
                    σ=float(input("Enter new σ :"))
                elif choice in ["5","stop"]:
                    break
                else:
                    print("Enter the right operation")
        elif change=="no":
            break
        else:
            print("Enter the right operation")
    try:
        r*=10**-3
        slope=float(input("Enter the slope:"))
        tm= (slope/(2*p*r*Σ*σ))+T
        Tm=tm**0.25
        print(f"Tm is:{Tm}K")
    except ValueError as e:
        print("Invalid input,please enter a number") 
def RC_law():
    type=input("Enter the type of RC:\n1.charge\n2.discharge\n").lower()
    try:
        if type in ["1","charge"]:
            Vmax=float(input("Enter Vmax in volt:"))
            Vt=Vmax*0.63
            print(f"Vt is:{Vt}v")
        elif type in ["2","discharge"]:
            Vmax=float(input("Enter Vmax in volt:"))
            Vt=Vmax*0.37
            print(f"Vt is:{Vt}v")
        else:
            print("Please write the right type")
    except ValueError as e:
        print("Invalid input,please enter a number") 
def Black_body_law():
    m=79
    s=0.418
    a=44.68
    Σ=1
    while True:
        change=input(f"Do you wanna change any of these constants?\n1.Mass={m}gm\n2.Specific heat={s}J/gm.c\n3.Area={a}cm2\n4.Σ={Σ}\nYes or No?").lower()
        if change=="yes":
            while True:
                choice=input(f"Enter the constant you wanna change:\n1.Mass={m}gm\n2.Specific heat={s}J/gm.c\n3.Area={a}cm2\n4.Σ={Σ}\n5.stop\n").lower()
                if choice in["1","mass","m"]:
                    m=float(input("Enter new Mass in gm:"))
                elif choice in ["2","specific heat","specific","heat","h","sh"]:
                    s=float(input("Enter new specific heat in J/gm.c:"))
                elif choice in ["3","area","a"]:
                    a=float(input("Enter new Area in cm2:"))
                elif choice in ["4","Σ","sigma"]:
                    Σ=float(input("Enter new Σ :"))
                elif choice in ["5","stop"]:
                    break
                else:
                    print("Enter the right operation")
        elif change=="no":
            break
        else:
            print("Enter the right operation")
    try:
        t1=float(input("Enter T.1 in celsius:"))
        t2=float(input("Enter T.2 in celsius:"))
        t3=float(input("Enter T.3 in celsius:"))
        t4=(t1+t2+t3+273)**4
        t=(t1+t2+t3)/3
        T=(t+273)**4
        slope1=float(input("Enter slope1 c/sec:"))
        slope2=float(input("Enter slope2 c/sec:"))
        slope3=float(input("Enter slope3 c/sec:"))
        slope4=float(input("Enter slope4 c/sec:"))
        slope5=float(input("Enter slope5 c/sec:"))
        slope6=float(input("Enter slope6 c/sec:"))
        Slope=(slope1+slope2+slope3+slope4+slope5+slope6)/6
        Slope/=60
        σ=(m*s*Slope)/(a*Σ*(t4-T))
        print("σ is:",σ)
    except ValueError as e :
        print("Invalid input,please enter a number") 
def main():
    print("\n✨ Welcome to our physics calculator ✨\t")
    while True:
        choice=input("\nEnter the law you wanna calculate:\n1.packing factor law\n2.Thermistor law\n3.Melting point law\n4.Rc law\n5.Black body law\n6.Exit\n").lower()
        if choice in ["1", "packing factor law","packing factor","packing"]:
            packing_factor_for_cubic_system()
        elif choice in ["2", "thermistor law","thermistor"]:
            thermistor_law()
        elif choice in ["3", "melting point law","melting point ","melting"]:
            melting_point_law()
        elif choice in ["4", "rc law","rc"]:
            RC_law()
        elif choice in ["5", "black body law","black body","black"]:
            Black_body_law()
        elif choice in ["6", "exit"]:
            print("Bye Bye Butterfly🦋")
            time.sleep(5)
            break
        else:
            print("Please enter a valid option")
            continue
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again == "no":
            print("Bye Bye Butterfly🦋")
            time.sleep(5)
            break
        elif again == "yes":
            continue
        else:
            print("Please Enter Yes or No")
            return
main() 

            
    
    