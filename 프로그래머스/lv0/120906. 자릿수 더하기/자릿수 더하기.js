function solution(n) {
    return (""+n).split('').map( v => +v ).reduce( (acc,v) => acc+v )
}