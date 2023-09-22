function solution(board, k) {
    return board.reduce((acc,arr,indexA) => {
        arr.forEach( (n,indexB) => indexA+indexB <= k && (acc += n)  )
        return acc;
    },0);
}