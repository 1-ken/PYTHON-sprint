open = True
while open ==True:
  print("welcom to a basic calculator \n  I can perform the following operatios: \n + \n - \n *  \n / \n Enter the operator:")
  choosetheoperator =input()
  a = int(input("Enyer the first number:"))
  b = int(input("Enyer the second number:"))
  if choosetheoperator == "+":
    print(a+b)
  elif choosetheoperator == "-":
    print(a-b)
  elif choosetheoperator == "*":
    print(a*b)
  elif choosetheoperator == "/":
    print(a/b)
  else:
    print("Invalid operator")
    