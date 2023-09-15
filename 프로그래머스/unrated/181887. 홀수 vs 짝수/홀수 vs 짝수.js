function solution(num_list) {
    const {even, odd} = num_list.reduce( (acc,n,i) => ({ ...acc, [i%2 ? 'odd' : 'even']:acc[i%2 ? 'odd' : 'even'] + n }),{even:0, odd:0});
    return Math.max(even,odd);
}