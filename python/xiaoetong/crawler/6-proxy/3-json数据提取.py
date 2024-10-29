data = {

    "l1" : {

        "d1" : [{

            "t1":{
                "author":"a",
                "age":"18"
            },

            "t2":{
                "author":"b",
                "age":"19"
            },

            "t3":{
                "author":"c",
                "age":"20"
            }

        }]

    },

    "l2" : {
        "author": "d"
    }

}

import jsonpath

# $ root vertex
# ..  any path
# . offvertex
print(jsonpath.jsonpath(data, '$.l1.d1.age'))
print(jsonpath.jsonpath(data, '$..author'))

# jsonpath方法：返回值：
# 匹配成功：一个列表
# 匹配失败：False
