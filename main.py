"""
Given a String as input, replace all digits in the string by #. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "@4mn8*"
Output-> @#mn#*
"""

def recur(st):
  ln = len(st)
  if ln ==0:
    return ""
  e = st[0]
  if (e>='0' and e<='9'):
    return "#" + recur(st[1:])
  else:
    return e + recur(st[1:])

st = "@4mn8*"
print(recur(st))