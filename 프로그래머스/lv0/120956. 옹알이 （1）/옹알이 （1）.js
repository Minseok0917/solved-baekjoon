function solution(babbling) {
    return babbling.filter( value => 
        value
            .replace(/aya/,'@')
            .replace(/ye/,'@')
            .replace(/woo/,'@')
            .replace(/ma/,'@')
            .replace(/\@/g,'')
            .length  === 0
    ).length;
}