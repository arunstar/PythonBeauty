
def find_intersection():
    result = []
    for item in nums1:
        if item in nums2:
            result.append(item)
    return result


nums1 = [1,2,1]
nums2 = [2,2,2,1,5,7,8,9]
# print(find_intersection())


def find_dup(nums):
    seen =set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return nums[i]
        else:
            seen.add(nums[i])

nums = [1,3,4,2,2]

# print(find_dup(nums))


class Solution:
    def findDuplicate(self, nums):
        def store(nums,cur):
            print(nums)
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)

        return store(nums, 0)

# print(Solution().findDuplicate([1,3,4,2,2]))

class Solution(object):
    def get_intersection(self,s1,s2):
            return [x for x in s1 if x in s2]

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
    
        if len(nums1) < len(nums2) or len:
            return self.get_intersection(nums1,nums2)
        else:
            return self.get_intersection(nums2,nums1)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1,nums2))