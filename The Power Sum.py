x = int(input())
n = int(input())
comb = 0

def count_comb (sum_ , i,exp):
    global comb
    if sum_==0:
        comb += 1
        return

    if sum_ <0 or i**exp>sum_:
        return

    count_comb(sum_ , i+1 , exp)
    sum_ -= pow(i,exp)
    count_comb(sum_,i+1 , exp)

count_comb(x , 1,n)
print(comb)