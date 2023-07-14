function solution(a, b) {
    const next = +(""+a+b);
    const prev = +(""+b+a);
    return next > prev ? next : prev;
}