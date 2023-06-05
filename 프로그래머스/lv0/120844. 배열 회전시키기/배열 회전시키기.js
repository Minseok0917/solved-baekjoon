function solution(numbers, direction) {
    if(direction === 'left'){
        numbers.push(numbers.shift());
        return numbers;
    }else{
        return [numbers.pop(),...numbers];
    }
}