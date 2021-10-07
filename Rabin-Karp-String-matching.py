#String matching algorithm
#Rabin-Karp algo

d=10
def search(pattern, text, q):
    m=len(pattern) #length of pattern
    n=len(text) #length of original string- text
    p=t=i=j=0 #p and t are initial hash values for pattern and text
    #i and j are counters
    h=1

    for i in range(m-1):
        h=(h*d)%q #h to be used further in caculating hash value of sliding text window

    for i in range(m):
        p=(d*p + ord(pattern[i])) % q #calculate the hash value of pattern
        t=(d*t + ord(text[i])) % q #calculate the hash value of text

    #Find the match
    #slide the pattern over text one by one
    for i in range(n-m+1):
        #comparing the hash values for pattern and text
        if p==t:
            #if yes, comparing each character one by one
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break #if comparision fails then break out of loop
                
            #else, increment the value of j by 1
            j += 1
            # if p == t and pattern[0...m-1] = text[i, i + 1, ...i + m-1]
            if j==m:
                print("pattern found at: ", (i+1))
                
        #calculate the value of next window
        if i<(n-m):
            t=(d*(t-ord(text[i])*h)+ord(text[i+m]))%q

            #might get negative values of t, converting it to positive
            if t<0:
                t=t+q

#Driver Code              
text="ABCDEABDJJEDABDJJEOABDJFJAB"
pattern="AB"
q=13 #any prime number
search(pattern, text, q)
