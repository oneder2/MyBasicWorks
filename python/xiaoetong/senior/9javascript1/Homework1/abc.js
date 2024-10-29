let number = prompt("请输入成绩：");
let string = "";

if(0 <= number && number < 60){
    string = "不及格";
}else if(60 <= number && number < 70){
    string = "及格";
}else if(70 <= number && number < 80){
    string = "良好";
}else if(80 <= number && number < 90){
    string = "优秀";
}else if(90 <= number && number <= 100){
    string = "完美";
}else{
    string = "输入错误";
}

alert(string);