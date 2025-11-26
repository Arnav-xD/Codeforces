m,n = map(int,input("enter the weights of limak and bob: ").split()) 
year = 0 
while m <= n : 
    m = m*3
    n = n*2
    year += 1 
print(year)