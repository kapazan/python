count=0
num_list=[]
while count < 5:
  number= int(input('Please enter the number: '))
  num_list.append(number)
  count = count +1
def findLargestNum(nums):
  largest = nums[0]
  for i in nums:
    if i > largest:
      largest = i
  return largest
print(findLargestNum(num_list))