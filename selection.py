# This program is the code to Selection Sort
l=[]
a=int(input("enter the size of the array: "))
for _ in range(a):
    r=int(input())
    l.append(r)
# Actual code
for i in range(a):
    # Find the minimum element in remaining
    # unsorted array

    min_i=i
    for j in range(i+1,a):
        if l[min_i]>l[j]:
            min_i=j
            #Swap the found min element with the first element
            l[i], l[min_i]=l[min_i],l[i]
print("Sorted Array:",l)

