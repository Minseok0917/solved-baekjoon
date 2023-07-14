const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', line => {
    const isEven = (+line)%2 === 0;
    console.log(`${line} is ${isEven ? 'even' : 'odd'}`)
})