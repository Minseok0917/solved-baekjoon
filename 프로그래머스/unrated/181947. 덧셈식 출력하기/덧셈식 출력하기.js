const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', line => {
    const [a,b] = line.split(' ').map(Number);
    console.log(`${a} + ${b} = ${a+b}`);
});