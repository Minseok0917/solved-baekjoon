function solution(num_list) {
    const {합, 곱} = num_list.reduce( (acc,n) => ({
        합:acc['합']+n,
        곱:acc['곱']*n,
    }),{ 합:0, 곱:1 });
    return 합**2 > 곱 ? 1 : 0;
}