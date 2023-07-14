const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', line => {
    console.log(line.split('').map( char => {
        const isUpper = char === char.toUpperCase();
        return isUpper ? char.toLowerCase() : char.toUpperCase();
    }).join(""));
})