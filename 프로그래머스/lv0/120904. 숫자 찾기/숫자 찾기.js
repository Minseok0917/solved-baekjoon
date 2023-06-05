function solution(num, k) {
    const i = (""+num).indexOf(k);
    return i < 0 ? i : +i+1 ;
}