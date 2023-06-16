function solution(progresses, speeds) {
    return progresses
        .map( (progress,index) => Math.ceil((100-progress)/speeds[index]) )
        .reduce( (acc,day) => {
            if(acc.max < day){
                acc.max = day;
                acc.index++;
                acc.answer[acc.index] = 1;
            }else{
                acc.answer[acc.index] +=1;
            }
            return acc;
        },{
            max:0,
            index:-1,
            answer:[]
        }).answer;
}