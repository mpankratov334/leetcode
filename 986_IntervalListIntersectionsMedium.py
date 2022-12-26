"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and
secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].
"""

class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
      """ O(n+m) """
        i, j, ans = 0, 0, []
        while i < len(a) and j < len(b):
            if a[i][1] < b[j][0]:
                i += 1
            elif b[j][1] < a[i][0]:
                j += 1
            else:
                ans.append([max(a[i][0], b[j][0]), min(a[i][1], b[j][1])])
                if a[i][1] < b[j][1]:
                    i += 1
                else:
                    j += 1
        return ans

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
      """ O((n+m)log(n+m) """
        l1, l2 = len(firstList), len(secondList)
        zipped = []
        ans = []
        for pair in firstList:
            zipped.append((pair[0], 0, 'l1'))
            zipped.append((pair[1], 1, 'l1'))
            
        for pair in secondList:
            zipped.append((pair[0], 0, 'l2'))
            zipped.append((pair[1], 1, 'l2'))

        zipped.sort()
        lz = len(zipped)
        print(zipped)
        is_open1, is_open2 = False, False
        i = 0
        now = [-1] * 2
        while i < lz:
            if zipped[i][1] == 0:
                if zipped[i][2] == 'l1':
                    is_open1 = True
                else:
                    is_open2 = True
            else:
                if zipped[i][2] == 'l1':
                    is_open1 = False
                else:
                    is_open2 = False
            if is_open1 and is_open2:
                now[0] = zipped[i][0]
            elif now[0] != -1:
                now[1] = zipped[i][0]
                ans.append(now)
                now = [-1] * 2
            i += 1
        return ans
    
