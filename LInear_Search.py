def linear_Search(arr,Target):
    for index,value in enumerate(arr):
        if Target==value:
            return index
    return -1
   
   
   
arr=[3,21,0,6,33,21]
Target=6
result=linear_Search(arr,Target)
if result!=-1:
    print(result)
else:
    print("Element Not Found")