function solution(numbers, n) {
    let answer = 0;
    let index=0;
    while(answer <= n){
        answer += numbers[index];
        index++;
    }
    return answer;
}