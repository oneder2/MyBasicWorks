function fnshow(name, age){
    alert(name + "今年" + age + "岁" + "，今天星期四")
}

// // 创建定时器
// let btn = document.getElementById("input1");
// btn.addEventListener("click", function(){
//     let tid = setTimeout(fnshow, 1000, "李四", 12);
// })

// 清除定时器
function fnstop(){
    clearTimeout(btn);
}

// 给按钮添加函数：点击清除定时器
let btn1 = document.getElementById("input1");
btn1.addEventListener("click", function(){
    fnstop();
})

// setInterval重复调用指定函数
let btn = document.getElementById("input1");
setInterval(fnshow, 3000, "李四", 12);




