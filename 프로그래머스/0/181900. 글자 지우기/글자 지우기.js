function solution(my_string, indices) {
    return my_string.split('').filter( (_,index) => !indices.includes(index) ).join('')
}