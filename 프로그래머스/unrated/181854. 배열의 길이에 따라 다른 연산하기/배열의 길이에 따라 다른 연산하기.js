function solution(arr, n) {
    return arr.map( (m,i) => {
        if( arr.length%2 === 0 && i%2 || arr.length%2 && i%2 === 0){
            return m+n;
        }
        return m;
    })
}