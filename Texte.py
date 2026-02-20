#cauculadora basica
while True:
       cauculo=input("tipo do calculo ")
    if calculo==0:
      print("somente numeros")
      break
    a=int(input("numero 1")) 
    b=int(input("numero 2"))
    if cauculo == "+":
       print (a+b)
    elif cauculo== "/":
       print (a/b)
    elif cauculo==("-"):
       print (a-b)
    elif cauculo==("×"):
       print (a*b)