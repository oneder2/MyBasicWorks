# 题目一

### 题干

利用所学的css知识，尽可能实现下列的效果（两节css课，不局限于哪节课）：

![image-20240725150611222](C:\Users\陈怼怼\AppData\Roaming\Typora\typora-user-images\image-20240725150611222.png)

### 提示：

> /* 实心的边框 */
>
> border-style: solid;
>
> /* 边框的厚度 */
>
> border-width: ;
>
> /* 边框的圆角 */
>
> border-radius: ;
>
> /* 水平居中显示 */
>
> text-align: center;
>
> 能实现效果就行，不管啥属性

### 参考答案

~~~html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        .index {
            width: 500px;
            height: 500px;
            background-color: cornsilk;
            /* 实心的边框 */
            border-style: solid;
            /* 边框的厚度 */
            border-width: 10px;
            /* 边框的圆角 */
            border-radius: 30px;
            
            
        }

        .loginFont {
            /* 水平居中显示 */
            text-align: center;

        }

        .s1 {
            /* 内边距 padding*/
            padding: 20px;
        }

        .s2 {
            /* 设置字体大小 */
            font-size: 15px;
        }

        .input {
            width: 75%;
            height: 30px;
        }

        .submit {
            width: 417px;
            height: 37px;
            background-color: skyblue;
        }

        .s3 {
            font-size: 15px;
            color: red;

        }
    </style>
</head>

<body>
    <div class="index">
        <h1 class="loginFont">登录页面</h1>
        <div class="s1">
            <span class="s2">账户</span>
            <input type="text" class="input" placeholder="请输入用户名">
        </div>
        <div class="s1">
            <span class="s2">密码</span>
            <input type="password" class="input" placeholder="请输入用户密码">
        </div>
        <div class="s1">
            <span class="s2">邮箱</span>
            <input type="email" class="input" placeholder="请输入用户邮箱">
        </div>
        <div class="s1">
            <input type="submit" class="submit">
        </div>
        <div class="s1">
            <a href="zhuce.html">点击前往注册页面</a>
        </div>
        <div class="s3">
            <input type="radio"><span>已阅读并同意以下服务协议、隐私权政策、法律声明及客户端服务协议</span>
        </div>
    </div>

</body>

</html>
~~~

