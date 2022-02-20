"""List utils!"""
__author__ = "730389944"


def only_evens(nums: list[int]) -> list[int]:
    res: list[int] = []
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            res.append(nums[i])
    return res


def sub(nums: list[int], start: int, stop: int) -> list[int]:
    res: list[int] = []
    if start < 0:
        start = 0
    if stop > len(nums):
        stop = len(nums)
    if len(nums) == 0 | start > len(nums) | stop <= 0:
        return res
    for i in range(start, stop):
        res.append(nums[i])
    return res


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    res: list[int] = []
    for elt in first_list:
        res.append(elt)
    for elt in second_list:
        res.append(elt)
    return res