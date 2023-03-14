function solution(s){
    var answer = true;
    let stacks = [];
    for(let char of s){
        if(char === "("){
            stacks.push(char);
        }else if(char === ")"){
            if( stacks.length === 0 ) return false;
            stacks.pop();
        }
    }
    return stacks.length === 0;
}