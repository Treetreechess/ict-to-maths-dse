import math

def fibonacci_seq(Term):
    a = (1/2)*(1 + math.sqrt(5))
    return math.trunc(math.sqrt(1/5)*(a**(Term) - (-a)**(-Term)))

while True:
    Mode = input("Type of sequence(A = Arithmetic Sequence,F = Fibonacci Sequence,J = General Sequence):")

    if Mode == "A":
        # Arithmetic Sequence
        while True:
            Term_of_Na = int(input("Na th term of sequence:"))
            Na = int(input("Integer of Na th term:"))
            Term_of_Nb = int(input("Nb th term of sequence:"))
            Nb = int(input("Integer of Nb th term:"))
            if Term_of_Na == Term_of_Nb or Na == Nb:
                print("Terms of sequence and integers of term cannot be the same. Please Re-enter.")
                continue
            else:
                break
        Find_Term = int(input("Input Finding Term:"))
        Common_Difference = (Na - Nb)/(Term_of_Na - Term_of_Nb)
        NOne = Na - (Common_Difference * (Term_of_Na-1))
        Result = NOne + (Common_Difference * (Find_Term-1))
        print("Integer of "+str(Find_Term)+" th term is :",str(int(Result)))
    
    elif Mode == "F":
        # Fibonacci Sequence
        while True:
            Term_of_Na = int(input("Na th term of sequence:"))
            Na = int(input("Integer of Na th term:"))
            Term_of_Nb = int(input("Nb th term of sequence:"))
            Nb = int(input("Integer of Nb th term:"))
            if Term_of_Na == Term_of_Nb or Na == Nb:
                print("Terms of sequence and integers of term cannot be the same. Please Re-enter.")
                continue
            else:
                break
        Find_Term = int(input("Input Finding Term:"))
        Fa1 = fibonacci_seq(Term_of_Na - 2)
        Fa2 = fibonacci_seq(Term_of_Na - 1)
        Fb1 = fibonacci_seq(Term_of_Nb - 2)
        Fb2 = fibonacci_seq(Term_of_Nb - 1)
        NOne = ((Nb*Fa1) - (Na*Fb2)) / ((Fb1*Fa2) - (Fa1*Fb2))
        NTwo = ((Na)-(Fa1*NOne))/(Fa2)
        if Find_Term == 1:
            Result = NOne
        elif Find_Term == 2:
            Result = NTwo
        else:
            Result = fibonacci_seq(Find_Term - 2) * NOne + fibonacci_seq(Find_Term - 1) * NTwo
        print("Integer of "+str(Find_Term)+" th term is :",str(int(Result)))
        
    if Mode == "J":
        # General Sequence
        Term_of_Na = int(input("Na th term of sequence:"))
        Na = int(input("Integer of Na th term:"))
        Integeral_n = int(input("Integeral part of n of adding dots:"))
        Constant = int(input("Constant part of adding dots:"))
        Find_Term = int(input("Input Finding Term:"))
        Result = Na
        if Term_of_Na < Find_Term:
            for n in range(Term_of_Na,Find_Term):
                Result += ((Integeral_n*n) + Constant)
        elif Term_of_Na > Find_Term:
            for n in range(Term_of_Na-1,Find_Term+1,-1):
                Result -= ((Integeral_n*n) + Constant)
        print("Integer of "+str(Find_Term)+" th term is :",str(int(Result)))    
        
    command = input("Quit? (Input \"Q\" to Quit):")
    if command == "Q":
        break
       
    # elif Mode == "G":
    #     # Geometry Sequence