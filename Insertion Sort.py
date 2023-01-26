# https://youtu.be/K0zTIF3rm9s
# Insertion Sort

def sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j>=0 and key < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key

nums = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
sort(nums)

print(nums)