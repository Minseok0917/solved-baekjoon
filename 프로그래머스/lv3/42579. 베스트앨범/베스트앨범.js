 function solution(genres, plays) {
    const answer = [];
    const m = {};
    const m2 = {};
    for(let index in genres){
        const key = genres[index];
        const play = plays[index];
        m[key] = [...m[key]||[],{play,index}];
        m2[key] = (m2[key]||0)+play;
    }
    const ranking = Object.entries(m2);
    ranking.sort( (a,b) => b[1]-a[1] );
    console.log(m2);
    console.log(m);
    ranking.forEach( ([key]) => {
    	m[key].sort( (a,b) => b.play === a.play ? a.index - b.index : b.play - a.play );
        for(let i in m[key]){
            if( i >=2 ) break;
            answer.push(+m[key][i].index);
        }
    });
    
    return answer;
    
} 
