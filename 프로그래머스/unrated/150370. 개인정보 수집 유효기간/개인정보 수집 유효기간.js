function solution(today, terms, privacies) {
    const [year,month,day] = today.split('.').map(Number);
    const _today = dayAll(year,month,day);
    const _temrs = Object.fromEntries(terms.map( term => term.split(' ')));
    return privacies.map((private,id) => ({private,id })).filter( ({private}) => {
        const [privateDate,term] = private.split(' ');
        const [year,month,day] = privateDate.split('.').map(Number);
        const _private = dayAll(year,month,day);
        const _term = _temrs[term]*28
        
        return _private+_term <= _today;
    }).map( ({id}) => id+1 );
}
function dayAll(year,month,day){
    return (year*12*28)+(month*28)+(day);
}