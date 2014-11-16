#V = Vo + at
#V^2 = Vo^2 + 2ax
#x = Vot + .5at^2
#x = ((Vo+Vf)/2)*t
import math

x = raw_input("Enter Angle or Displacement: ")
Vo = raw_input("Enter Angular Velocity or Translational Velocity: ")
a = raw_input("Enter Angular Acceleration or Translational Acceleration: ")
Vf = raw_input("Enter Final V or Final Omega: ")
t = raw_input("Enter Time: ")

if(a):
	a = float(a)
if(x):
	x = float(x)
if(Vo):
	Vo = float(Vo)
if(t):
	t = float(t)
if(Vf):
	Vf = float(Vf)

if x and a and Vo:
	Vf = ((Vo*Vo)+(2*a*x))**.5
	t = (Vf-Vo)/a

elif x and Vo and Vf:
	a = ((Vf*Vf)-(Vo*Vo))/(2*x)
	t = (Vf-Vo)/a

elif x and Vo and t:
	a = (x-(Vo*t))*2/(t**2)
	Vf = Vo + (a*t)

elif x and a and Vf:
	Vo = ((Vf*Vf)-(2*a*x))**.5
	t = (Vf-Vo)/a

elif x and a and t:
	Vo = (x-(.5*a*(t*t)))/t
	Vf = Vo + (a*t)

elif x and Vf and t:
	Vo = (x-(.5*a*(t*t)))/t
	a = (x-(Vo*t))*2/(t**2)

elif Vo and a and Vf:
	t = (Vf-Vo)/a
	x = (Vo*t)+(.5*a*t*t)

elif Vo and Vf and t:
	x = ((Vo+Vf)/2)*t
	a = (x-(Vo*t))*2/(t**2)

elif a and Vf and t:
	Vo = Vf-(a*t)
	x = ((Vo+Vf)/2)*t

else:
	print "ERROR1"

if a and t and Vo and Vf and x:
	dic = {"Acceleration":a, "Time":t, "Initial Velocity":Vo, "Final Velocity":Vf, "Displacement":x}
	keys = dic.keys()
	for var in keys:
		print var.":\t\t".dic[var]
else:
	print "ERROR2"