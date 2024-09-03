from typing import List

def challenge1(array1: List[str], array2: List[str], array3: List[str]) -> List[str]:
  """
  Given three ordered arrays of arbitrary length containing random capital letters, write an algorithm
  which returns the longest ordered array which all arrays share!

  Example
  Given the sequence ADDZ and CDDY and UDDF the longest shared array is DD.

  Example
  Given the sequence UIBAZDBSIAHFB, PQACIZDBIBDLAG and QIDBCZDBKSHDVF, the longest
  shared array is ZDB.
  """
  def is_subsequence(subseq: List[str], arr: List[str]) -> bool:
    """ Check if subseq is a subsequence of arr """
    it = iter(arr)
    return all(el in it for el in subseq)
  
  def generate_subsequences(arr: List[str]) -> List[List[str]]:
    """ Generate all subsequences of arr """
    subsequences = [[]]
    for item in arr:
      subsequences += [seq + [item] for seq in subsequences]
    return subsequences
  
  # Generate all subsequences of array1
  subsequences = generate_subsequences(array1)
  
  # Filter subsequences that are also subsequences of array2 and array3
  valid_subsequences = [
    subseq for subseq in subsequences
    if is_subsequence(subseq, array2) and is_subsequence(subseq, array3)
  ]
  
  # Return the longest valid subsequence
  return max(valid_subsequences, key=len, default=[])
