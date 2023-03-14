function solution(s){
    let count = 0;
    for(let char of s){
        if(char === "("){
            count+=1
        }else if(count){
            count-=1
        }else{
            return false;
        }
    }
    return count === 0;
}