button1=input(" button 1 enter on/off:")
button2=input("button 2 enter on/off:")
condition=input("please enter series or parallel:")
if button1=="on" and button2=="on" and condition=="series":
    print("light on")
elif button1=="off" and button2=="on" and condition=="series":
    print("light off")
elif button1=="on" and button2=="off" and condition=="series":
    print("light off")
elif button1=="off" and button2=="off" and condition=="series":
    print("light off")
elif button1=="on" and button2=="off" and condition=="parallel":
    print("light on")
elif button1=="off" and button2=="on" and condition=="parallel":
    print("light on")
elif button1 == "off" and button2=="off" and condition=="parallel":
    print("light off")
elif button1 == "on" and button2=="on" and condition=="parallel":
    print("light on")
else:
    print("wrong input")

