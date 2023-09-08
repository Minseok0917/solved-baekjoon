function solution(n) {
    const m = Math.sqrt(n);
    return Number.isInteger(m) ? (m+1)**2 : -1;
}