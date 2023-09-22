function solution(arr, [[a1,b1],[a2,b2]]) {
    return [...arr.slice(a1,b1+1),...arr.slice(a2,b2+1)];
}