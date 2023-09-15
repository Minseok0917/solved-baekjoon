function solution(num_list) {
    const end0 = num_list.at(-1);
    const end1 = num_list.at(-2);
    num_list.push(end0 > end1 ? end0 - end1 : end0*2);
    return num_list;
}