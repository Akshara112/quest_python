#to find the valid count of p separating the array into two such that all elements in the first array is greater than p and all elements in second array less than p
integers_n, value_of_x, value_of_y = map(int,input().split())
               #2<=n<=2000,x,y>=1
               #x+y=n
array = list(map(int,input().split()))



def possible_count_of_p(integers_n, value_of_x, value_of_y,array):
    array.sort()

    p_count = 0



    for i in range (1,integers_n):
        p=(array[i-1] + array[i])/2
        
        if array[i-1]<p<array[i]:
            p_count += 1

    return p_count

print(possible_count_of_p(integers_n, value_of_x, value_of_y, array))   
    
    

    




