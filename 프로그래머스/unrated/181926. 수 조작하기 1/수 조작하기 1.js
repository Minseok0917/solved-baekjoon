function solution(n, control) {
    const {w,s,d,a} = [...control].reduce( (acc,c) => ({...acc, [c]:(acc[c]??0)+1 }),{});
    return n + w*1 + s*-1 + d*10 + a*-10;
}