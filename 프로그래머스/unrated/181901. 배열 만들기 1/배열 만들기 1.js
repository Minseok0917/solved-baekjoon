function solution(n, k) {
    return Array(parseInt(n/k)).fill(k).map( (k,i) => k*(i+1) )
}