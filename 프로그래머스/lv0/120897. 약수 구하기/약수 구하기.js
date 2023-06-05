function solution(n) {
    let array = [1];
    for(let i=2; i<=n; i++){
        if( n%i === 0  ) array.push(i);
    }
    array.sort( (a,b) => a-b );
    return array;
}