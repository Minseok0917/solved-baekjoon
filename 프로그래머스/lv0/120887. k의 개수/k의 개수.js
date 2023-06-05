function solution(i, j, k) {
    let result = ''
    for(let m=i; m<=j; m++){
        result = result + (""+m)
    }
    return result.split("").map( v => +v ).filter( v => v === k ).length;
}