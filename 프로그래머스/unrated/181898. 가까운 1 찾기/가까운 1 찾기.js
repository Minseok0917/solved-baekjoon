function solution(arr, idx) {
    let count = 0;
    for(let index in arr){
        if(index < idx ) continue;
        if(arr[index])  return +index;
    }
    return -1;
}