function solution(emergency) {
    emergencyA = [...emergency];
    emergency.sort( (a,b) => b-a );
    const mmmmmmm = Object.fromEntries(emergency.map( (v,i) => [v,i+1] ))
    return emergencyA.map( v => mmmmmmm[v] );
}