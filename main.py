# Built-in imports
def reverse(text):
  """
  takes input and reverses it
  
  Parameters
  text: str -- name of input
  
  Return
  string which is the reversed version of text/input"""
  if len(text) <= 1:
    return text
  return reverse(text[1:]) + text[0]

def is_palindrome(string):
  """ 
  takes input and checks if it is a palindrome 

  Parameters
  string: str -- name of input

  Return
  boolean True/False
  """
  string = str(string).strip(" ")
  if len(string) <= 1:
    return True
  if string[0] == string[-1]:
    return(is_palindrome(string[1:-1]))
  else:
    return False

