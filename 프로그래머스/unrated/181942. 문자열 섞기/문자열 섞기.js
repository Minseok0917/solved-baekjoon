function solution(str1, str2) {
    let str = '';
    str1 = str1.split('');
    str2 = str2.split('');
    while(str1.length > 0 || str2.length > 0 ){
        str += str1.shift() || "";
        str += str2.shift() || "";
    }
    return str;
}