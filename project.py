#implementation of Tic Toc Toe game.
n=int(input("enter order of the game"))
#li is the list which stores the values of tic toc toe game.
li=[]
#setting default values as -1
for i in range(0,n):
    a=[]
    for j in range(0,n):
        a.append(-1)
    li.append(a)
#displaying board.   
def display_row(li,i):
    for j in range(0,n):
        if j==n-1:
            print(li[i][j])
        else:
            print(li[i][j],"|",end=" ")

def display_verti(n):
    for i in range(0,n):
        print("---",end=" ")
    print()
def display(li):
    for i in range(0,n):
        display_row(li,i)
        print()
        if i==n-1:
            break;
        display_verti(n)
#function for checking the rows.
def row_check(li):
    c=0
    for i in range(0,n):
        for j in range(0,n):
            k=li[i][0]
            if( k!=-1):
                if li[i][j]==k:
                    c=c+1
        if(c==3):
            return True
        else:
            c=0
    return False
#function for checing diagnol.
def diagonal_check(li):
    c=0
    for i in range(0,n):
        k=li[0][0]
        for j in range(0,n):
            if i==j and k!=-1:
                if k==li[i][j]:
                    c=c+1
    if c==3:
        c=0
        return True

    else:
        return False
#function for colown checking.
def colown_check(li):
    c=0
    i=0
    while i<n:
        k=li[0][i]
        for j in range(0,n):
            if(k!=-1):
                if li[j][i]==k:
                    c=c+1
                    print("")
        if(c==3):
            return True
        else:
            c=0
        i=i+1
    return False
#function for checking reverse digonal.
def reverse_check(li):
    c=0
    for i in range(0,n):
        k=li[0][n-1]
        for j in range(0,n):
            if i==(n-j-1)and k!=-1:
                if k==li[i][j]:
                    c=c+1
    if c==3:
        c=0
        return True
    else:
        return False                       
print("welcome to TIC TOK TOE game of order{}".format(n))
print()
display(li)
c=0
d=False
#Game code.
while(c<(n*n)):
    if c%2==0:
        print("player 1 enter choice 'S'")
    else:
        print("player 2 enter choice 'O'")
    i=int(input("enter i value"))
    j=int(input("enter j value"))
    if i<n and j<n:
        k=input("enter your choice")
        if li[i][j]==-1:
            li[i][j]=k
            display(li)
            if row_check(li)==True or diagonal_check(li) or colown_check(li) or reverse_check(li):
                if(c%2==0):
                    print("----- Player1 won the Game---")
                else:
                    print("----Player2 won the Game---")
                d=True
                break
            c=c+1    
        else:
            print("this is already taken")
    else:
        print("enter value less than {}".format(n))
if d==False:
    print("---Match Drawn Play again---")
