function solution(progresses, speeds) {
    const clearn = [];
    const answer = [];
    let max = -1;
    let buildCount = 0;
    for(let index in progresses){
        const progress = progresses[index];
        const speed = speeds[index];
        const day = Math.ceil((100-progress)/speed);
        if(max < day){
            if(max > -1) answer.push(buildCount);
            max = day;   
            buildCount = 1;
        }else{
            buildCount +=1;
        }
    }
    answer.push(buildCount);
    return answer;
}