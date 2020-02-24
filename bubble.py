def bubble(arr, dim):
    alg_count = [0, 0]
    for i in range(0,dim-1):
        j = dim-1
        while j>i:
            alg_count[0]+=1
            if arr[j]<arr[j-1]:
                alg_count[1]+=1
                arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return alg_count
