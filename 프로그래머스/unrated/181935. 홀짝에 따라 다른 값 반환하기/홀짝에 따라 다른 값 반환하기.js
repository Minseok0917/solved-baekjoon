function solution(n) {
    const isEven = n%2 === 0;    
    let sum = isEven ? 0 : 1;
    for(let index=2; index<=n; index++){
        if(isEven && !(index%2)){
            sum += index**2;
        }else if(!isEven && index%2){
            sum += index;   
        }
    }
    return sum;
}