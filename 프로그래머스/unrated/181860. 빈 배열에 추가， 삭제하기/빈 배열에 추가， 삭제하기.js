function solution(arr, flag) {
    const answer = [];
    flag.forEach( (isFlag,index) => {
        for(let i=0; i<arr[index]; i++) isFlag ? answer.push(arr[index],arr[index]) : answer.pop();
    })
    return answer;
}