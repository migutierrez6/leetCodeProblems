nums = [4, 7, 11, 15, 5]
target = 9


def twoSum(nums, target):
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        print(f'this is i {i}')
        print(f'this is n {n}')
        diff = target - n
        print(f'this is diff = {diff}')
        if diff in prevMap:
            return [prevMap[diff], i]
        else:
            prevMap[n] = i
            print(prevMap)
            print("")
    return


print(twoSum(nums, target))
