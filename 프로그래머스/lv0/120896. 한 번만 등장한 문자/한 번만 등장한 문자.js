function solution(s) {
    return Object.entries(s.split('').reduce( (acc,value) => ({
        ...acc,
        [value] : (acc[value] || 0 ) +1
    }),{})).filter( ([key,count]) => count === 1 ).map( ([key]) => key ).sort().join("")
}