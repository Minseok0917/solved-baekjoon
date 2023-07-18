const operation = {
    true:(a,b) => a+b,
    false:(a,b) => a-b,
};

function solution(a, b, flag) {
    return operation[flag](a,b);
}