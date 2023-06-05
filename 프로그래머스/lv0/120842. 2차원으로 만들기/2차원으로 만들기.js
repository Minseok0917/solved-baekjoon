function solution(num_list, n) {
    let array = [];
    for(let i=0; i<Math.ceil(num_list.length/n); i++){
        array.push( num_list.slice(i*n,i*n+n) )
    }
    return array;
}