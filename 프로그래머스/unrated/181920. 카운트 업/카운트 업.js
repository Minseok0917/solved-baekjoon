function solution(start, end) {
    return Array.from( Array(end-start+1), (_,index) => start+index );
}