function solution(my_string, s, e) {
    let answer = ``;
    answer += my_string.slice(0,s);
    answer += [...my_string].slice(s,e+1).reverse().join('');
    answer += my_string.slice(e+1);
    return answer;
}