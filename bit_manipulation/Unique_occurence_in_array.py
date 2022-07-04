'''The aim of this program is to find out thee number which occurs
only 1 time in an array in which all other elements occurs twice
USING BITWISE'''

array = list(map(int,input("Enter the elements of the array:").split()))
if len(array) ==0:
    print("PLease enter a non-zero length array")
else:
    num=array[0];
    for i in range(1,len(array)):
        num^=array[i]
print("The number occuring only 1 time is :",num)

