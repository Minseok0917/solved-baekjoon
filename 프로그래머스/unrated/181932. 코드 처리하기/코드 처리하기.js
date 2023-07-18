function solution(code) {
    return code.split('').reduce( (acc,char,index) => {
        if(char === '1') return {...acc, mode:!acc.mode};
        if(!acc.mode && index%2 === 0) acc.str += char;
        else if(acc.mode && index%2 !== 0) acc.str += char;
        return acc;
    },{mode:false, str:''}).str || 'EMPTY';
}