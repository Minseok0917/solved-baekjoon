function solution(my_string, num1, num2) {
    const strs = my_string.split('');
    const ns1 = strs[num1];
    const ns2=  strs[num2];
    strs[num1] = ns2;
    strs[num2] = ns1;
    return strs.join('');
}