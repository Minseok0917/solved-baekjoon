function solution(my_string, m, c) {
    let index=0;
    let answer="";
    while(index<my_string.length){
        answer+=my_string[index+c-1];
        index+=m;
    }
    return answer;
}