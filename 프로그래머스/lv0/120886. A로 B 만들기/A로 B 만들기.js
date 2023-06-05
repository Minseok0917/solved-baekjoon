function solution(before, after) {
    const beforeText = before.split('').sort( (a,b) => a.charCodeAt()-b.charCodeAt() ).join('');
    const AfterText = after.split('').sort( (a,b) => a.charCodeAt()-b.charCodeAt() ).join('');
    return beforeText === AfterText ? 1 : 0
}