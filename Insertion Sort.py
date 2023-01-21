# https://youtu.be/nCNfu_zNhyI
# Insertion Sort

def sort(nums):
    for i in range(1, len(nums)):
        anchor = nums[i]
        j = i - 1
        while j>=0 and anchor < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = anchor
        
        print(nums)

nums = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
sort(nums)

print(nums)