function solution(strArr) {
    return strArr.map( (s,i) => i%2 ? s.toUpperCase() : s.toLowerCase() );
}