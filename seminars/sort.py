from fontTools.ttLib.tables.G_M_A_P_ import table_G_M_A_P_

A=[15,13,9,23,6,1,11,7]
def bubble_sort(arr):
    N=len(arr)
    for i in range (N):
        for j in range(N-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
def insert_sort(arr):
    N = len(arr)
    for i in range(N):
        tmp=arr[i]
        j=i-1
        while j>=0 and tmp< arr[j]:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=tmp
    return arr
def select_sort(arr):
    N = len(arr)
    for i in range(N-1):
        min=1000000
        for j in range(i,N):
            if arr[j]<min:
                min=arr[j]
                min_index=j
        tmp=arr[i]
        arr[i]=min
        arr[min_index]=tmp
    return arr
def merge(A,B):
    len_a=len(A)
    len_b = len(B)
    C=[]
    i=0
    j=0
    while i<len_a or j<len_b:
        if i>=len_a:
            C.append(B[j])
            j+=1
            continue
        if j >= len_b:
            C.append(A[i])
            i += 1
            continue
        if A[i] <B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j+=1
    return C




def merge_sort(arr):
      N=len(arr)
      if N==1:
          return arr
      ind=N//2
      L=arr[0:ind]
      R=arr[ind:]
      return merge(merge_sort(L),merge_sort(R))
print(merge_sort(A))

