function solution(surveys, choices) {
    const scores = Object.fromEntries([...'RTCFJMAN'].map( (n) => [n,0]));
    const getCategory = (keyA,keyB) => scores[keyA] >= scores[keyB] ? keyA : keyB;

    surveys.forEach( (survey,index) => {
        const [left,right] = survey;
        const choiceIndex = choices[index];
        const group = select(left,right,choiceIndex);
        const score = getScore(choiceIndex);
        scores[group] += score;
    });
    
    return getCategory('R','T') + getCategory('C','F') + getCategory('J','M') + getCategory('A','N');
}

function select(left,right,index){
    return index < 4 ? left : right;
}

function getScore(index){
    if(index === 4) return 0
    if(index > 4) return index - 4;
    return -(index-4);
}