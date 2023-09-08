function solution(n){
    return [...(""+n)].map(Number).reduce( (a,v) => a+v);
}