// 理应是这么写的，因为直接用区间长度除以除数就等于可被整除的数字个数。届时用变量替代即可
// alert(100/5);

let number = 100;
let count = 0;

for(let i = 1; i <= number; i++){
    if(i % 5 == 0){
        count++;
    }
}

alert(count);