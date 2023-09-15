function solution(arr1, arr2) {
    if(arr1.length > arr2.length) return 1;
    if(arr1.length < arr2.length) return -1;
    
    const arrSum1 = arr1.reduce( (acc,n) => acc+n )
    const arrSum2 = arr2.reduce( (acc,n) => acc+n )
    
    if(arrSum1 > arrSum2) return 1;
    if(arrSum1 < arrSum2) return -1;
    return 0
}
