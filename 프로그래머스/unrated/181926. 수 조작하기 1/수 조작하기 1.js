function solution(n, control) {
    const o = { w:1, s:-1, d:10, a:-10};
    return [...control].reduce( (acc,c) => acc+o[c] ,n);
}