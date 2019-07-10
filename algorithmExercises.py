# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 你需要返回给定数组中的重要翻转对的数量。

# 示例 1:
# 输入: [1,3,2,3,1]
# 输出: 2

# 示例 2:
# 输入: [2,4,3,5,1]
# 输出: 3
# 注意:

# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。


list1=[1,3,2,3,1]

class Solution:
    def reversePairs(self, nums: 'List[int]') -> 'int':
        def merge_and_count(lo, hi):
            if lo == hi:
                return 0

            count = 0
            mid = (lo + hi) // 2
            count += merge_and_count(lo, mid) + merge_and_count(mid + 1, hi)
            left = lo
            right = mid + 1
            while left <= mid and right <= hi:
                if nums[left] > 2 * nums[right]:
                    # 如果我们找到了有效对，则left和mid之间的元素也将是有效对。计算这些元素
                    count += mid - left + 1
                    # 增加右指针以检查左侧元素是否可以与其中任何一个匹配
                    right += 1
                else:
                    left += 1
            # 核心
            nums[lo: hi + 1] = sorted(nums[lo: hi + 1])  # 排序是因为 mid 左右两边在比较的时候可以,节省时间，否则需要 o(n^2)

            return count

        if not nums:
            return 0

        return merge_and_count(0, len(nums) - 1)




def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)/2
    left = merge_sort(lists[:int(middle)])
    right = merge_sort(lists[int(middle):])
    print("-------------")
    print(left)
    print(right)
    return merge(left, right)


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(merge_sort(a))


# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 示例:
# 输入: "Hello World"
# 输出: 5
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        str_list = []
        word_count = []
        if len(s) == 0:
            pass

        else:
            for index, value in enumerate(s):
                if value == " ":
                    if len(str_list) == 0:
                        pass
                    else:
                        word_count.append(len(str_list))
                        str_list = []

                else:
                    str_list.append(value)
                    if index == len(s) - 1:
                        word_count.append(len(str_list))
        if len(word_count) == 0:
            return 0
        else:
            return word_count[-1]