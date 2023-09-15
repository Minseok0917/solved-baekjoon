function solution(num_list) {
    const left = +num_list.filter( n => n%2 === 0 ).join('');
    const right = +num_list.filter( n => n%2 !== 0 ).join('');
    return left+right;
}