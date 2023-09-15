function solution(num_list, n) {
    const answer = [];
    while(num_list.length){
        const [a] = num_list.splice(0,n);
        answer.push(a);
    }
    return answer;
}