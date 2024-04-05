# Built-in imports
def reverse(text):
  """
  takes input and reverses it
  
  Parameters
  text: str -- name of input
  
  Return
  string which is the reversed version of text/input"""
  char = ""
  if len(text) <= 1:
    return text + char
  char = text[0]
  text = text[1:]
  return reverse(text) + char

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
    string = string[1:-1]
    return(is_palindrome(string))
  else:
    return False

