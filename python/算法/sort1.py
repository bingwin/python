# -*- coding: utf-8 -*-

# 冒泡排序的时间复杂度是O(N^2)
#
# 冒泡排序的思想: 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换位置
#
# 比如有五个数: 12, 35, 99, 18, 76, 从大到小排序, 对相邻的两位进行比较
#
# 第一趟:
# 第一次比较: 35, 12, 99, 18, 76
# 第二次比较: 35, 99, 12, 18, 76
# 第三次比较: 35, 99, 18, 12, 76
# 第四次比较: 35, 99, 18, 76, 12

# 每次把最大或者最小的选出来
# 冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 也就是说要进行n-1趟操作(已经归位的数不用再比较)

def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,45,6,8,2,1]

print bubbleSort(nums)


# 插入排序
# 先固定一个数，再选其他一个的数与它比较，高在上面，低在下面，再选其他的一个数与前两个比较，高在上，低在下，中间就在中间

def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        x = arr[i]
        for j in range(i,-1,-1):
            # j为当前位置，试探j-1位置
            if x < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                # 位置确定为j
                break
        arr[j] = x
    return arr

# def printArr(arr):
#     for item in arr:
#         print(item)

arr = [4, 7 ,8 ,2 ,3 ,5]
print(insertSort(arr))
# printArr(arr)


# 归并排序首先将数组分成相等的一半，然后以排序的方式组合它们。参考以下代码实现
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))

