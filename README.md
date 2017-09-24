# polynomial-calculator
Python command line program to create an nth degree polynomial, evaluate the polynomial at a particular value, calculate and evaluate the 1st derivative at a particular value, calculate and evaluate a definite integral at a particular value, and calculate RAM approximations.

## Running the Polynomial Calculator
1. Install python.
1. Download main.py.
1. Type `python main.py`.
1. Follow the prompts.

## Example output of an LRAM on a 3rd degree polynomial.

=> python main.py
This program calculates values, derivatives, exact definite
integrals, and definite integral approximations for polynomials
of a degree and coefficients determined by the user.

Please enter the degree of your polynomial: 3

Please enter the coefficient of the monomial of degree 3: 2

Please enter the coefficient of the monomial of degree 2: -1

Please enter the coefficient of the monomial of degree 1: 4

Please enter the coefficient of the monomial of degree 0: 5.5

Your polynomial is associated with the given dictionary. Each
key of the dictionary is the degree of the monomial
and the value is the coefficient of the associated degree.

{0: 5.5, 1: 4.0, 2: -1.0, 3: 2.0}

Choose one of the following:

  v: value

  d: derivative

  i: integral

  r: RAM (Riemann Approximation Method)

==> r

Please enter the lower bound for the integral: 2

Please enter the upper bound for the integral: 2.75

Please enter the number of steps: 5

Would you like to see the coordinates? y for yes and anything else for no: y

(2.0, 25.5)

(2.15, 29.354249999999997)

(2.3, 33.744)

(2.45, 38.70975000000001)

(2.6, 44.292)

(2.75, 50.53125)

Would you like a LRAM, RRAM, or TRAM approximation? Enter the type of ram: LRAM

The approximate integral for this LRAM over 5 steps on the interval from  2.0  to  2.75  on the polynomial  {0: 5.5, 1: 4.0, 2: -1.0, 3: 2.0}  is  33.3196875
