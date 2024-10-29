# 题目一

### 题干

有以下代码，请创建一个html，复制代码到pycharm中：**要求补全script里面的代码**

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>敲木鱼</title>
    <style>

        .box1_01 {
            margin: auto;
        }

        #gongDe {
            font-family: 楷体;
            font-size: 80px;
            color: red;
        }

        #vip {
            /* 50是上下边距  120是左右边距*/
            margin: 50px 120px;
            width: 80px;
            height: 80px;
            background-color: green;
            color: white;
        }
    </style>
</head>

<body>

        <div class="box1_01">
            <img id="button" src="https://img.keaitupian.cn/newupload/12/1670919763991586.gif">
            <br><!-- 图片和按钮都是块级标签 -->
            <div id="gongDe">
                功德:
                <span>0</span>
            </div>
           <input type="button" id="vip" value="+1">
        </div>

    <script>
    //     /*实现点击图片,让功德数字+1
    //     */
    </script>
</body>
</html>
```

![image-20240801060920459](C:\Users\陈怼怼\AppData\Roaming\Typora\typora-user-images\image-20240801060920459.png)

请实现点击`加1`，功德会不断加：效果如下：

![image-20240801061106353](C:\Users\陈怼怼\AppData\Roaming\Typora\typora-user-images\image-20240801061106353.png)

### 参考答案

~~~html

~~~









## 题目二（选做，不需要交）

### 题干

在第一题基础上实现以下效果：

1、**点击自动按钮，功德开始自动加**，

2、**此时自动按钮变成结束按钮，点击结束按钮后，停止自动加1**

代码还是一样的，input标签的value可以改成**自动**

```
<input type="button" id="vip" value="自动">
```

![image-20240801143114834](C:\Users\陈怼怼\AppData\Roaming\Typora\typora-user-images\image-20240801143114834.png)

![image-20240801143131581](C:\Users\陈怼怼\AppData\Roaming\Typora\typora-user-images\image-20240801143131581.png)