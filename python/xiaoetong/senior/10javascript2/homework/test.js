// 题目一
// 长方形的面积
function area(width, height) {
    let area = width * height;

    return area;
}

console.log(area(100, 100));

// 题目二
// fill函数
let array1 = [0, 0, 0, 0, 0];
array1.fill(7, 1, 5);

console.log(array1);

// 题目三
// copyWithin函数
let array2 = [1,2,3,4,5];
array2.copyWithin(0, 1, 5);

console.log(array2);

// 题目四
// {n, 2n, 3n, 4n, 5n}
function multiply(num){
    let array3 = [];
    for (let i = 1; i <= 5; i++) {
        array3.push(i * num);
    }
    return array3;
}

console.log(multiply(1));
