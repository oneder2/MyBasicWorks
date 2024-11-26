from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals
    
    ans = []
    i = 0
    intervals = sorted(intervals, key=lambda x: x[0])
    append_pair = intervals[0]
#    print(intervals)

    for i in range(0, len(intervals)-1):
#        print(append_pair)
#        print(intervals[i+1])

        # 如果不存在重叠
        # 1. 原右小于下一个左
        # 2. 原左大于下一个右
        # 添加区间
        if (append_pair[0] > intervals[i+1][1]) or (append_pair[1] < intervals[i+1][0]):
#            print("不重叠")
            ans.append(append_pair)
            append_pair = intervals[i+1]
        
        # 如果存在重叠
        # 1. 原左小于下一个左，并且原右大于下一个左
        # 2. 原右大于下一个右，并且原左小于下一个右
        # 3. 原左小于下一个左，并且原有大于下一个右
        else:
#            print("重叠")
            append_pair = [min(append_pair[0], intervals[i+1][0]), max(append_pair[1], intervals[i+1][1])]

        
#        print(append_pair)
#        print("______")
    
    ans.append(append_pair) # 该右值合法

    return ans


inputList = [[2,3],[4,5],[6,7],[8,9],[1,10]]
exception = [[1,4], [0,1]]
#print(merge(inputList))
#print(merge(exception))
#x,y = inputList[0]
#print(x, y)
