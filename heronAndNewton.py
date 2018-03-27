#Heron's Method for Calculating Square Roots
#Stub by JP Brichta, March 2018
#
#Heron's method for calculating square roots is approximately 2000 years old and was devised by Hero of Alexandria. It is an
#iterative method (meaning that it uses a previous answer to calculate the next) that in principle, will continue forever.
#When using iterative method, it is important to decide if the answer is "good enough" or if the program should continue.
#You can read more about Heron's Method and other methods of computing square roots in the wikipedia entry here:
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
#

def heron(x, accuracy = 0.001):
  """Compute the square root of the number x using Heron's method. The accuracy is defaulted to three decimal places, but you
  can use a larger or smaller number if you wish. The smaller the number, the more time the calculation will take."""
  g = x / 2
  while abs((g**2) - x) > accuracy:
      g = 0.5*(g + (x/g))
  return g

def newton3(x, accuracy = 0.001):
  """Finds the cube root of a number based off Newton's
   method""" 
  g = x / 2
  while abs((g**3) - x) > accuracy:
    g = g - (((g**3) - x) / (3 * (g**2)))
  return g

def newton2(x, accuracy = 0.001):
  """Finds the square root of a number based off Newton's
   method""" 
  g = x / 2
  while abs((g**2) - x) > accuracy:
    g = g - (((g**2) - x) / (2 * g))
  return g
