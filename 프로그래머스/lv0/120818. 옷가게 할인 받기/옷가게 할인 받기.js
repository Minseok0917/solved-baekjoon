function solution(price) {
    const percent = (price >= 500_000 ? 20 :
            price >= 300_000 ? 10 :
            price >= 100_000 ? 5 : 0)
    return parseInt(price-price/100*percent)
}