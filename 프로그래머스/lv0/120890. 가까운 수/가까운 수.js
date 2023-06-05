function solution(array, n) {
    const a = array.map( v => ({
        v,
        m:n-v < 0 ? v-n : n-v
    }) ).sort( (a,b) =>  a.m- b.m );
    let fm = a[0].m;
    const a2 = a.filter( ({m}) => fm === m ) .sort( (a,b) => a.v - b.v  );
    return a2[0].v
}