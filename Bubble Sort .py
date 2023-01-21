# https://youtu.be/Vca808JTbI8
# Bubble Sort

def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
sort(nums)

print(nums)