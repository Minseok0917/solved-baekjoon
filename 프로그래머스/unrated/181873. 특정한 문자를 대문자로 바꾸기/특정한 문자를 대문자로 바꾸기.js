function solution(my_string, alp) {
    const r = new RegExp(alp,'g');
    return my_string.replace(r,alp.toUpperCase())
}