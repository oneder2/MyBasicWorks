// 获取按钮元素
let btn1 = document.getElementById('vip');
// 获取span元素
let span1 = document.getElementById('span1');

// 给按钮添加点击事件
btn1.onclick = function(){
    stateSwitch();
}

function addOne(){
    span1.innerText = String(Number(span1.innerText) + 1);
}

// 点击一次按钮，数字加1
function stateSwitch(){
    let timer = null;
    if(btn1.value == "开始"){
        btn1.value = "停止";
        timer = setInterval(addOne, 1000);
    }else{
        btn1.value = "开始";
        clearInterval(timer);
    }
}