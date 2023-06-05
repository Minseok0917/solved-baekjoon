function solution(numbers) {
    return (numbers.reduce( (acc,value) => acc+value) / numbers.length).toFixed(1)
}