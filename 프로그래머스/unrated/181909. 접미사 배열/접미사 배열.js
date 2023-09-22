function solution(my_string) {
    return Array.from( Array(my_string.length), (_,idx) => my_string.slice(idx) ).sort()
}