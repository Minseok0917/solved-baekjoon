function solution(arr) {
    return arr.reduce( (acc,n) => ([...acc,...Array(n).fill(n)]),[]);
}