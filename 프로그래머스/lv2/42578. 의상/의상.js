function solution(clothes) {
    return Object.values(clothes.reduce( (acc,[cloth,part]) => ({ ...acc, [part]:acc[part]+1 || 1 }),{})).reduce( (acc,value) => acc*(value+1),1)-1;
}