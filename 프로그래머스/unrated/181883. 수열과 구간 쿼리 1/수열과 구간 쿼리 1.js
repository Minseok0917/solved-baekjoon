function solution(arr, queries) {
    queries.forEach( ([s,e],i) => {
        Array.from(Array(e-s+1),(_,i) => arr[s+i]=arr[s+i]+1 )
    });
    return arr;
}