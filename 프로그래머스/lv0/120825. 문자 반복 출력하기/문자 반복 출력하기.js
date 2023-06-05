function solution(my_string, n) {
    return my_string.split('').map( v => v.repeat(n) ).join('')
}