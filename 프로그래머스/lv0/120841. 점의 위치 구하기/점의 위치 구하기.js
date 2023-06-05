function solution([x,y]) {
    var answer = 0;
    const upX = x > 0;
    const upY = y > 0;
    return (
        upX && upY ? 1 : 
        upX && !upY ? 4 : 
        !upX && upY ? 2: 3
    )
}