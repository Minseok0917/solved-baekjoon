function solution(myString) {
    return [...myString].map( c => c.charCodeAt() < 108 ? 'l' : c ).join('');
}