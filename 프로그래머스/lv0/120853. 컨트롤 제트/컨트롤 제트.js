function solution(s) {
    return s
        .split(' ')
        .filter( (n,i,s) => ![n,s[i+1]].includes('Z'))
        .reduce( (acc,n) => acc+Number(n),0)    
}