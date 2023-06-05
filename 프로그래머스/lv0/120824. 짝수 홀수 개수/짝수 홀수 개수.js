function solution(num_list) {
    return num_list.reduce( ([even,odd],v) =>  {
        if( v%2 === 0 ) even++
        else odd++
        return [even,odd];   
    },[0,0])
}