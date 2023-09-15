function solution(my_string, index_list) {
    return index_list.map( n => my_string[n] ).join('')
}