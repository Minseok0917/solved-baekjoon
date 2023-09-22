function solution(my_string) {
    return Array.from( Array(my_string.length), (_,idx) => my_string.slice(my_string.length-idx-1,my_string.length) ).sort()
}