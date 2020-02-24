import random
def select (arr, dim):
    alg_count=[0,0]
    for i in range(0,dim-1):
        minindex=i              #miniindex = 0
        for j in range(i+1,dim):    # j с первого после i до последнего
            alg_count[0]+=1
            if arr[minindex]>arr[j]:        #Если arr[0]> arr[1]
                minindex=j                  # ТО miniindex = j(1)
                alg_count[1]+=1             
        arr[i],arr[minindex]=arr[minindex],arr[i]       #В конце, меняются местами
    return alg_count
