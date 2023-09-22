function solution(arr, queries) {
    queries.forEach( ([s,e],i) => {
        while(s<=e) arr[s++]++;
    });
    return arr;
}