function solution(my_string, overwrite_string, s) {
    const strs = my_string.split('');
    for(let index=0; index<overwrite_string.length; index++){
        strs[index+s] = overwrite_string[index];
    }
    return strs.join('');
}