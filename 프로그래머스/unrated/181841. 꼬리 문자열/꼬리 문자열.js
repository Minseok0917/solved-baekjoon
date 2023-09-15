function solution(str_list, ex) {
    return str_list.filter( c => !c.includes(ex) ).join('')
}