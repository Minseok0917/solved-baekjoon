function solution(priorities, location) {
    let index = 0;
    const answer = [];
    const mm = [...priorities].sort( (a,b) => b-a );
    priorities = priorities.map( (v,i) => ({v,i}) );
    while(mm.length){
        if( priorities[index].v >= mm[0] ){
            if(priorities[index].i === location){
                return answer.length+1;
            }
            answer.push(priorities[index])
            mm.shift();
        }else{
            priorities.push(priorities[index]);
        }
        index++;
    }
    
}