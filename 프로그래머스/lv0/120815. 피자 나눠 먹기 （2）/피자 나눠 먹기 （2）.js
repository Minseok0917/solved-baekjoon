function solution(n) {
    for(let i=1; i<=100; i++){
        if(6*i%n === 0 ){
            return i
        }
    }
}