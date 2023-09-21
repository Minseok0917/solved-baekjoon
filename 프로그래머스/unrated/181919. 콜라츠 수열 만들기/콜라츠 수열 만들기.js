function solution(n) {
    let arr = []
    while(true){
        arr.push(n);
        if(n === 1) break;
        if(n%2 === 0){
            n/=2;
            continue;   
        }
        n = 3*n+1;
    }
    return arr;
}