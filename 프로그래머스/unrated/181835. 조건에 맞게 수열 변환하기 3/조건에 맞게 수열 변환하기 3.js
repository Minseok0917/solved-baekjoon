function solution(arr, k) {
    const isEven = k%2 === 0;
    return arr.map( (n) => isEven ? n+k : n*k );
}