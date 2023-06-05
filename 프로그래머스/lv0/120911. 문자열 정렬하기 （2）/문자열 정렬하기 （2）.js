function solution(my_string) {
    my_string = my_string.toLowerCase().split('');
    my_string.sort( (a,b) => a.charCodeAt()-b.charCodeAt() )
    return my_string.join("")
}