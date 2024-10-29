// 通过id获取元素
let op = document.getElementById('p1')
console.log(op);

// 通过选择器获取元素
let oa = document.querySelector('.father');
console.log(oa);

// 通过选择器获取元素
let ob = document.querySelectorAll('div');
console.log(ob);

// 获取并改变标签内容与属性
// innerText:获取或者修改元素内的文字，不包含标签和样式
// innerHTML:获取或者修改元素内的内容，包含标签和样式
// value:获取或者修改元素的值

// 获取元素内容
let a1 = document.getElementById('a1');
console.log(a1.innerText);
a1.innerText = '大家每天都很开心';
 
let a2 = document.getElementById('a2');
console.log(a2.innerHTML);

