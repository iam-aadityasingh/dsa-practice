def moveZeroes(self, nums: list[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                if i != index:
                    nums[index], nums[i] = nums[i], nums[index]
                index += 1