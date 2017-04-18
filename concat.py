myVarRed= "Red"
myVarBlue= "Blue"

print("Roses are Red. " + "Violets are Blue.")
print("Roses are " + myVarRed + ". Violets are " + myVarBlue)

myStr = "Roses are Red. " + "Violets are Blue."
varStr = "Roses are " + myVarRed + ". Violets are " + myVarBlue

print(myStr)
print(varStr)

name = "Joe"
feet= 6
inches= 2

print("My name is " + name + ". I'm " + str(feet) + " feet " + str(inches) + " inches tall.")
myStr = "My name is " + name + ". I'm " + str(feet) + " feet " + str(inches) + " inches tall."
print(myStr)

#------------------------

name = "Mary"
number = 1

print "Concat with \+ and stringifying var number:"
print name + " had " + str(number) + " little lamb."
print "\nConcat with \, and NOT stringifying var number:"
print name,"had",number,"little lamb."
