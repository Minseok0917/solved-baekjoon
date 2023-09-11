function solution(number) {
    let count = 0;
    while(number.length > 2){
        for(let indexA=1; indexA<number.length; indexA++){
            for(let indexB=indexA+1; indexB<number.length; indexB++){
                const trio = number[0]+number[indexA]+number[indexB];
                if(trio === 0 ) count++;
            }
        }
        number.shift();
    }
    return count;
}