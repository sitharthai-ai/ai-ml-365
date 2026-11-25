
# Problem 1 

# count_vowels("Hello World")   # → 3
# count_vowels("PYTHON")        # → 1
# count_vowels("rhythm")        # → 0
# count_vowels("")              # → 0
# count_vowels("A1! e?")        # → 2


# def count_vowels(text):
#     vowels_count =0;
#     for i in text:  
#         if i in ("a","A", "e","E","i","I", "o","O","u","U"): 
#             vowels_count+=1;

#     return vowels_count




# print(count_vowels("Hello World"))
# print(count_vowels("PYTHON")    )    # → 1
# print(count_vowels("rhythm")  )      # → 0
# count_vowels("")              # → 0
# count_vowels("A1! e?")        # → 2

# --------------------------------------------------------------------

# Problem 2

# second_largest([4, 1, 7, 3])      # → 4
# second_largest([10, 10, 9])       # → 9
# second_largest([5, 5, 5])         # → None
# second_largest([2])               # → None
# second_largest([])                # → None
# second_largest([-3, -1, -2])      # → -2



# def second_largest(nums):
#     _2nd_largest = None;
#     unique_nums = list(set(nums))

#     if len(unique_nums) <=1 :
#         print(_2nd_largest)
#         return _2nd_largest

#     largest_num = max(unique_nums);
#     unique_nums.remove(largest_num);

#     _2nd_largest = max(unique_nums);
#     print(_2nd_largest)
#     return _2nd_largest



# second_largest([4, 1, 7, 3])      # → 4
# second_largest([10, 10, 9])       # → 9
# second_largest([5, 5, 5])         # → None
# second_largest([2])               # → None
# second_largest([])                # → None
# second_largest([-3, -1, -2])      # → -2


# ----------------------------------------------------------







# word_freq("The cat and the hat.")
# # → {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}

# word_freq("Hi! hi, HI?")
# # → {'hi': 3}

# word_freq("  data   science  ")
# # → {'data': 1, 'science': 1}

# word_freq("")
# # → {}



# -----------------------------------

# Fizz buzz FizzBuzz

# fizzbuzz(5)
# # → ['1', '2', 'Fizz', '4', 'Buzz']

# fizzbuzz(15)[-1]
# # → 'FizzBuzz'

# fizzbuzz(0)
# # → []


# def fizzbuzz(n):
#     if n==0:
#         return []
#     return_array=[];
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0 : 
#             return_array.append('FizzBuzz')

#         elif i%3==0: 
#             return_array.append('Fizz')

#         elif i%5==0:
#             return_array.append('Buzz')

#         else:
#             return_array.append(str(i))        

#     print(return_array)
#     return return_array

# fizzbuzz(5)
# # → ['1', '2', 'Fizz', '4', 'Buzz']

# fizzbuzz(15)[-1]
# # → 'FizzBuzz'

# fizzbuzz(0)
# # → []

# ---------------------------------------------------

# Two sum target




# def two_sum(nums, target):

#     return_array = []
#     if len(nums)<=1:
#         print(None)
#         return None

#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if(nums[i]+nums[j])==target:
#                 print([i,i+1])
#                 return [i,i+1]
#             elif(j==len(nums)-2)  :
#                 print(None)
#                 return None
#             else:
#                 continue


            
        
    






# two_sum([2, 7, 11, 15], 9)   # → [0, 1]
# two_sum([3, 2, 4], 6)        # → [1, 2]
# two_sum([3, 3], 6)           # → [0, 1]
# two_sum([1, 2, 3], 10)       # → None
# two_sum([], 5)               # → None