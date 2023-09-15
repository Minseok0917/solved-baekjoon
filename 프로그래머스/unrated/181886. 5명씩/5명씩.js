function solution(names) {
    const answer = [];
    while(names.length){
        const [name] = names.splice(0,5)
        answer.push(name);
    }
    return answer;
}