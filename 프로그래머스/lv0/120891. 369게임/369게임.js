function solution(order) {
    return (""+order).replace(/3|6|9/g,'@').replace(/[^@]/g,'').length
}