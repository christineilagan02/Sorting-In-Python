# https://youtu.be/5KjapFQNxUo
# Selection Sort

def sort(nums):

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
sort(nums)

print(nums)