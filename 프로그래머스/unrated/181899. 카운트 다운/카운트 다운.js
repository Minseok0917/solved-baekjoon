function solution(start, end_num) {
    return Array(start-end_num+1).fill(0).map( (n,i) => start-i );
}