function solution(number) {
    return [...number].reduce( (acc,n) => acc+(+n),0)%9
}