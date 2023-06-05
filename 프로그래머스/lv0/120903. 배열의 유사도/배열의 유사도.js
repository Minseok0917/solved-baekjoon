function solution(s1, s2) {
    return s1.filter( v => s2.some( v2 => v2 === v ) ).length
}