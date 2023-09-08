function solution(absolutes, signs) {
    return signs.reduce( (a,v,i) => a+(absolutes[i]*(v?1:-1)) ,0);
}