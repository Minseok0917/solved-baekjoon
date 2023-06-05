function solution(my_string) {
    return my_string.split('').map( s => s === s.toLocaleLowerCase() ? s.toUpperCase() : s.toLocaleLowerCase() ).join("");
}