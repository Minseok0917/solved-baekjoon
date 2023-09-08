function solution(left, right) {
    var answer = 0;
    while(left<=right){
        let count = 0;
        for(let n=1; n<=left; n++){
            count += left%n ? 0 : 1;
        }
        answer += count%2 ? -left++ : left++;
    }
    return answer;
}