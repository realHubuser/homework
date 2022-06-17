def bubble_sort(array):
    n=len(array)
    for i in range(0,n):
        need_sort = False
        for j in range(0,n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] # swap#import random
                need_sort = True

        if( False == need_sort):
            break
        print(array)


# def selectionSort(arr, size):\
   
#     for step in range(size):
#         min_idx = step

#         for i in range(step + 1, size):
         
           
#             if arr[i] < arr[min_idx]:
#                 min_idx = i
         
#         arr[step], arr[min_idx] = arr[min_idx], arr[step]

#  list=[64,25,12,22,11]
list1=[5,1,4,2,8]
print (list1)
bubble_sort(list1)
# selectionSort (list, len(list))
print (list1)
