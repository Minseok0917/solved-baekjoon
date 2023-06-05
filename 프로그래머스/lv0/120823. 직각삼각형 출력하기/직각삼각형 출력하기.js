const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = '';

rl.on('line', function (line) {
    const n = line;
    input = '';
    for(let i=0; i<n; i++){
        for(let j=n-i; j<=n; j++){
            input+='*';
        }
        input+='\n';
    }
    input = `${input.trim()}`;
}).on('close', function () {
    console.log(input);
});


