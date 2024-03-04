function solution(myString, pat) {
    return [...myString].reduce( (acc) => {
        acc += +myString.search(pat) === 0 
        myString = myString.slice(1)
        return acc;
    },0);
}