function solution(numLog) {
    const checking = (a,b) =>  (
        a+1 === b ? 'w' :
        a-1 === b ? 's' :
        a+10 === b ? 'd' :
        a-10 === b ? 'a' : ''
    )
    return numLog.map( (a,i) => checking(a,numLog[i+1]) ).join('');
}