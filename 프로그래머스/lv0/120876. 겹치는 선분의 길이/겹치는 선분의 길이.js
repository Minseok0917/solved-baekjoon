function solution(lines) {
    let counter = {};
    lines.forEach( ([start,end]) => {
        for(let x=start; x<end; x++){
            counter[x] = (counter[x] ?? 0) + 1;
        } 
    });
    return Object.values(counter).filter( n => n > 1 ).length
    
}