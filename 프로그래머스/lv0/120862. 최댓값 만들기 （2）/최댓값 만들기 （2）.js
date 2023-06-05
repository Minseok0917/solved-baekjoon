function solution(numbers) {
    numbers.sort( (a,b) => a-b )
    const start = parseInt(numbers[0]*numbers[1]);
    const end = parseInt(numbers.at(-1)*numbers.at(-2));
    return start > end ? start : end;
}