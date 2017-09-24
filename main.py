# Author: Griffin Hampton
#
# This program calculates derivatives, exact definite integrals,
# and definite integral approximations for polynomials of a fixed
# degree determined by the user.

# This class is used to represent a single monomial in a polynomial.
class Monnomial(object):
    def __init__(self, coef, degree):
        self.coef = coef
        self.degree = degree

    def __str__(self):
        return "coefficient =" + str(self.coef) + ", degree=" + str(self.degree)


# Evaluates a polynomial function at x
def evaluatePolynomial(x, dictionary):
    sum = 0
    for i in range(len(dictionary)):
        sum = sum + dictionary[i] * x ** i
    return sum


# Evaluates a derivative function at x
def evaluateDerivative(x, dictionary):
    sum = 0
    for i in range(len(dictionary) - 1):
        sum = sum + dictionary[i] * x ** i
    return sum


# Evaluates an integral function at x
def evaluateIntegral(x, dictionary):
    sum = 0
    for i in range(len(dictionary)):
        sum = sum + dictionary[i + 1] * x ** (i + 1)
    return sum


# Writes the polynomial in a dictionary form.
def createPoly(monomials):
    poly = dict([(f.degree, f.coef) for f in monomials])
    return poly


# Writes the derivative of the polynomial in dictionary form
def createDeriv(monomials):
    deriv = dict([(f.degree - 1, f.coef * f.degree) for f in monomials])
    return deriv


# Writes the integral of the polynomial in dictionary form
def createIntegral(monomials):
    integral = dict([(f.degree + 1, f.coef / (1 + f.degree)) for f in monomials])
    return integral


# everything below here is for integral approximations

# Creates a list of X values to use in a rectangular approximation method
def newSpace(initialValue, stepSize, numSteps):
    xValues = [initialValue]
    newXValue = initialValue + stepSize
    xValues = xValues + [newXValue]
    for i in range(numSteps - 1):
        newXValue = newXValue + stepSize
        xValues = xValues + [newXValue]
    return xValues


# Area function for a single rectangle in the integration chain
def calcArea(height, stepSize):
    return height * stepSize


def interval(start, end, n):
    spread = end - start
    stepsize = spread / n
    return [(x) * stepsize + start for x in range(n + 1)]


# Creates an array of monomials given degree.
def createMonomialArray(degree):
    monomialArray = []
    for i in range(degree + 1):
        print ""
        coef = float(input("Please enter the coefficient of the monomial of degree " + str(degree - i) + ": "))
        degreeMon = (degree - i)
        monomialArray = monomialArray + [Monnomial(coef, degreeMon)]
    return monomialArray


def chooseFunctionType():
    choiceList = ["v", "d", "i", "r"]
    print ""
    print "Choose one of the following:"
    print "   v: value"
    print "   d: derivative"
    print "   i: integral"
    print "   r: RAM (Riemann Approximation Method)"
    print ""

    choice = raw_input("==> ")

    while choice not in choiceList:
        print ""
        print "Your choice was not in the list of options (v, d, i, r) please try again."
        print ""
        choice = raw_input("==> ")
    return choice


def getInput():
    global DegreeOfPolynomial
    global MonomialArray
    DegreeOfPolynomial = int(input("Please enter the degree of your polynomial: "))
    MonomialArray = createMonomialArray(DegreeOfPolynomial)


def value():
    oneXvalue = int(input("Please enter the value you want to evaluate on the polynomial: "))
    return oneXvalue


def lowerbound():
    low = float(input("Please enter the lower bound for the integral: "))
    return low


def upperbound():
    high = float(input("Please enter the upper bound for the integral: "))
    return high


def steps():
    return int(input("Please enter the number of steps: "))


def pref():
    return raw_input("Would you like to see the coordinates? y for yes and anything else for no: ")


def chooseRAMtype():
    RAMlist = ["TRAM", "LRAM", "RRAM"]

    print ""

    RAM = raw_input("Would you like a LRAM, RRAM, or TRAM approximation? Enter the type of ram: ")
    RAM = RAM.upper()
    while RAM not in RAMlist:
        print ""
        RAM = raw_input("Please enter the string LRAM, RRAM, or TRAM: ")
        RAM = RAM.upper()
    return RAM


# ==============================================
# --- Main ---
print "This program calculates values, derivatives, exact definite \
integrals, and definite integral approximations for polynomials \
of a degree and coefficients determined by the user."
print ""
while True:
    getInput()
    poly = createPoly(MonomialArray)

    print ""
    print "Your polynomial is associated with the given dictionary. Each \
key of the dictionary is the degree of the monomial \
and the value is the coefficient of the associated degree."
    print poly

    while True:
        # Call the function getInput to get the user's raw_input.
        # Call another function type
        choice = chooseFunctionType()
        if choice == "v":
            xValue = value()
            answer = evaluatePolynomial(xValue, poly)
            print "the output for polynomial ", poly, " at value ", xValue, "is"
            print answer

        elif choice == "d":
            derivativeDictionary = createDeriv(MonomialArray)
            print ""
            print derivativeDictionary

            xValue = value()
            answer = evaluateDerivative(xValue, derivativeDictionary)
            print "The derivative for polynomial ", poly, " at value ", xValue, "is"
            print answer

        elif choice == "i" or "r":
            print ""
            low = lowerbound()
            hi = upperbound()

            if choice == "i":
                ID = createIntegral(MonomialArray)
                print ""
                print ID

                upperIntegral = evaluateIntegral(hi, ID)
                lowerIntegral = evaluateIntegral(low, ID)
                answer = upperIntegral - lowerIntegral
                print "The integral for polynomial ", poly, " on the bound ", low, " to ", hi, " is"
                print answer

            elif choice == "r":
                print ""
                numSteps = steps()
                print ""
                xValues = interval(low, hi, numSteps)
                yValues = []
                for i in range(len(xValues)):
                    yValue = evaluatePolynomial(xValues[i], poly)
                    yValues = yValues + [yValue]
                    coordinate = []
                for i in range(len(xValues)):
                    newCoordinate = [(xValues[i], yValues[i])]
                    coordinate = coordinate + newCoordinate

                print ""
                preference = pref()
                if preference == "y":
                    for i in range(len(coordinate)):
                        print(coordinate[i])
                else:
                    print ""

                RAM = chooseRAMtype()

                spread = hi - low
                stepSize = spread / numSteps

                integral = 0

                if RAM == "LRAM":
                    for i in range(len(yValues)):
                        yValue = yValues[i]
                        rectangularComponent = calcArea(yValue, stepSize)
                        integral = integral + rectangularComponent
                elif RAM == "RRAM":
                    for i in range(len(yValues) - 1):
                        yValue = yValues[i + 1]
                        rectangularComponent = calcArea(yValue, stepSize)
                        integral = integral + rectangularComponent
                elif RAM == "TRAM":
                    for i in range(len(yValues) - 1):
                        yValue = (yValues[i] + yValues[i + 1]) / 2
                        rectangularComponent = calcArea(yValue, stepSize)
                        integral = integral + rectangularComponent

                print ""

                print "The approximate integral for this " + RAM + " over \
" + str(numSteps) + " steps on the interval from ", low, " to \
", hi, " on the polynomial ", poly, " is ", integral

        print("")
        print("Would you like to run another function type?; (y) for yes, anything else for no:")
        yesNo = raw_input()
        print ""
        if yesNo != 'y':
            # Break out of the loop if the user is finished.
            break
    print("Would you like to run another polynomial for these functions?; (y) for yes, anything else for no:")
    yesNo = raw_input()
    print ""
    if yesNo != 'y':
        # Break out of the loop if the user is finished.
        break
