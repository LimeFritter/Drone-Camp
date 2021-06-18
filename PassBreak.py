#you can type anynumber of any length and this will guess it
password = input("type any number")
passLength = len(password)
passToGuess = []
compguess = []
compfinal = []
for q in range(passLength):
    passToGuess.append(int(password[q]))
    compguess = [0] * passLength
    compfinal = [0] * passLength

x = 0
for x in range(passLength):

    i=0
    for i in range (10):
    
        compguess[x] = i
        print(compguess)
        if compguess[x] == passToGuess[x]:
            compfinal[x] = compguess[x]
            
            
       
    
            
        

print(f"{compfinal} got it")