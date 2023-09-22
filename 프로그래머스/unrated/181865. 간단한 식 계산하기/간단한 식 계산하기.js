function solution(binomial) {
    const [a,op,b] = binomial.split(' ');
    const operators = { "+":(a,b) => a+b, "-":(a,b) => a-b, "*":(a,b) => a*b }
    return operators[op](+a,+b);
}