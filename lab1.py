
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   maxVal = -9999999999999999999999999  
   if int_list == None  :
      raise ValueError
   elif (len(int_list) == 0):
      return None
   else:
      for i in range( len(int_list)):
         if int_list[i] > maxVal:
            maxVal = int_list[i]
      return maxVal

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return []
   return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

   middleIdx = low +  (high - low) //2
   if( int_list == None or int_list[middleIdx] == None ):
      raise ValueError 
   if int_list[middleIdx] == target:
      return middleIdx
   elif  target < int_list[middleIdx] and low-high >0: 
      return bin_search(target, low , middleIdx -1, int_list)
   elif target > int_list[middleIdx]  and low-high >0: 
      return bin_search( target, middleIdx+1 , high, int_list)
   elif( (low-high) < 0 and int_list[middleIdx] != target ):
      print(low, high, middleIdx)
      return None
list_val =[0,1,2,3,4,7,9,10 ]
print(bin_search(1, 0 , len(list_val), list_val))
print(bin_search(1000, 0 , len( list_val), list_val))

# 0  1 2 3 4 5 6 7 9 10
#