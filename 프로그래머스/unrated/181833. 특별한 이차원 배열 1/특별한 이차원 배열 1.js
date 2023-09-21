function solution(n) {
    return Array.from( Array(n), (_,i) => {
        const array = Array(n).fill(0);
        array[i] = 1;
        return array;
    })
}