#defines cummulative sum array
def find_cummulative_sum(arr):
    #creates arr2 and appends
    arr2=[]
    arr2.append(arr[0])
    #adds array and puts it in array 2
    for i in range (1,len(arr)):
        arr2.append(arr2[i-1]+ arr[i])
    return arr2
#prints sum of new array
print(find_cummulative_sum([2,12,55,118]))
