function solution(a, b) {
    return a%2 && b%2 ? a**2 + b**2 : 
        a%2 || b%2 ? 2*(a+b) : Math.abs(a-b);
}