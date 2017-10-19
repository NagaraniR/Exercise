inputA = int('0101',2)
 
print "Before shifting " + str(inputA) + " " + bin(inputA)
print "After shifting in binary: " + bin(inputA << 1)
print "After shifting in decimal: " + str(inputA << 1)

#output
#Before shifting 5 0b101
#After shifting in binary: 0b1010
#After shifting in decimal: 10
