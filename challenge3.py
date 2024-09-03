from collections import Counter
from math import gcd
from functools import reduce

def challenge3(colors) -> int:
  """
  Assume an array of arbitrary length whose elements represent colors of the set blue (b), green (g) or
  yellow (y). Write an algorithm which returns the number of subsets in which the array can be split so
  that every subset contains equal color representations with the same length. Remark: The colors do
  not have to appear in equal order within the subsets.

  Example
  Given the array y-y-b-b-g-g, the algorithm will return 1 since the array can be split into one subset of
  length 6 which contains 2y, 2b and 2g elements.

  Example
  Given the array y-y-b-b-g, the algorithm will return 0 since no equal subsets can be found.

  Example
  Given the array y-b-g-g-b-y, the algorithm will return 3 since array of length 6 itself features equal color
  representation. When splitting the array into two sections of length three, two equal subsets can be
  identified: y-b-g and g-b-y.
  """

  n = len(colors)

  # Can't split an empty array
  if n == 0:
    return 0

  # Count each of the colors
  counts = Counter(colors)

  # Find all possible subsets of the array
  def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
  
  # Find the greatest common divisor (GCD) of the color counts
  color_gcd = reduce(gcd, counts.values())

  valid_subset_sizes = 0

  def is_valid_subset_size(subset_size):
    if subset_size == 0:
      return False
    num_subsets = n // subset_size

    return all(count % num_subsets == 0 for count in counts.values())

  # Check there is the same number of each color in each subset
  for divisor in find_divisors(n):
    if is_valid_subset_size(divisor):
      valid_subset_sizes += 1
  
  return valid_subset_sizes - 1
