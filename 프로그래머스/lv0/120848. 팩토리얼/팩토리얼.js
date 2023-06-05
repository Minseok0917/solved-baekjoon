function solution(n) {
    let prev = 1;
    for(let i=1; i<=10; i++){
        let total = 1;
        for(let j=1; j<=i; j++){
            total *= j;
        }
        if( total <= n ) prev = i;
        else break
    }
    return prev
}