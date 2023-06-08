function solution(bin1, bin2) {
    const total = before(bin1)+before(bin2);
    return after(total);
}
function before(bin){
    const length = bin.length;
    return bin.split('').map( (value,index) => value === '1' ? 2**(length-index-1)  : 0 ).reduce( (acc,value) => acc+value )
}
function after(n){
    let m = [];
    while(true){
        m.push(Math.floor(n%2));
        n = n/2;
        if( n < 1 ) break;
    }
    console.log(m)
    return m.reverse().join('')    
}