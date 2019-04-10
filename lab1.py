
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   maxVal = -9999999999999999999999999  
   if type(int_list) == None  :
      raise TypeError
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
   if type(int_list) == None:
      raise TypeError
   if len(int_list) == 0:
      return []
   return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

   middleIdx = low +  (high - low) //2
   if( type(int_list) == None or int_list[middleIdx] == None ):
      raise TypeError
   if int_list[middleIdx] == target and type(int_list[middleIdx]) == int :
      return middleIdx
   elif  target < int_list[middleIdx] and type(int_list[middleIdx]) == int : 
      return bin_search(target, low , middleIdx -1, int_list)
   elif target > int_list[middleIdx] and type(int_list[middleIdx]) == int : 
      return bin_search( target, middleIdx+1 , high, int_list)
   else:
      return None 