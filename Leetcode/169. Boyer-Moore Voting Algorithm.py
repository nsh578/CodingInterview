def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

        print("Candidate:", candidate)
        print("num:", num)
        print("count", count)
        print("")
        

    return candidate

print(majorityElement([2,5,23,5,2,6,2,513,632,7,3463,1,2,645,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2]))
