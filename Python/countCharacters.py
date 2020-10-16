#Count all lower case, upper case, digits, and special symbols from a given string

input_str = "P@#yn26at^&t0d@y"

def findcounts(input_str):
    charsCount = 0
    digitsCount = 0
    symbolsCount = 0
    
    for char in input_str:
        if char.islower() or char.isupper():
            charsCount = charsCount + 1
        elif char.isnumeric():
            digitsCount = digitsCount+1
        else:
            symbolsCount = symbolsCount + 1
            
    print("chars", charsCount, "Digits: ", digitsCount, "symbols: ", symbolsCount)
    
findcounts(input_str)   
        
