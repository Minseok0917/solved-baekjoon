function solution(a, b, c) {
    const ops = { 1:(a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3), 2: (a+b+c)*(a**2+b**2+c**2), 3:a+b+c }
    return ops[new Set([a,b,c]).size]
}