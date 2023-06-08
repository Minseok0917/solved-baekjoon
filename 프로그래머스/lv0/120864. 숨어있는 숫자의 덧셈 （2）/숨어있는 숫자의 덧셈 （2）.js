function solution(my_string) {
    return [...my_string.match(/[0-9]+/g) || [0]].map(Number).reduce( (acc,v) => acc+v)
}