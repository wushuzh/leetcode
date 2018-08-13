def twoSum2_cache(numbers, target):
    dic = {}
    for i, part in enumerate(numbers):
        prev_part = target - part
        if prev_part in dic:
            return [dic[prev_part]+1, i+1]
        dic[part] = i


def twoSum2_binary_search(numbers, target):
    for i in range(len(numbers)):
        l, r = i+1, len(numbers)-1
        wanted = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == wanted:
                return [i+1, mid+1]
            elif numbers[mid] < wanted:
                l = mid+1
            else:
                r = mid-1
