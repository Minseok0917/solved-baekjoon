function solution(myString, pat) {
    return +myString.includes([...pat].map( s => s === 'A' ? 'B' : 'A' ).join(''));
}