function solution(n) {
    let total = 0;
    for(let i=4; i<=n; i++){
        let count = 0;
        for(let j=1; j<=i; j++){
            if( i%j === 0 ) count +=1;
        }
        if(count >= 3) total +=1;
    }
    return total;
}