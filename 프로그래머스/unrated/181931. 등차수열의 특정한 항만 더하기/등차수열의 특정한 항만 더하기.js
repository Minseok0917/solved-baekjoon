function solution(a, d, included) {
    return included.reduce( (acc,include,index) => include ? acc+(a+d*index) : acc,0);
}