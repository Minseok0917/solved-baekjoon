function solution(ineq, eq, n, m) {
    const isLeft = ineq === '>';
    const isRight = ineq === '<';
    const isSame = eq === '=';
    if(isLeft && isSame)
        return +(n >= m);
    else if(isLeft && !isSame)
        return +(n > m);
    else if(isRight && isSame)
        return +(n <= m);
    else if(isRight && !isSame)
        return +(n < m);    
}