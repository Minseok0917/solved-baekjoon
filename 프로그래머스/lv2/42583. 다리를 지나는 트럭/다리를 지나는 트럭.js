function solution(bridge_length, weight, truck_weights) {
    const bridges = Array(bridge_length).fill(0);
    let currentWeight = 0;
    let second = 0;
    
    while(true){
        second += 1;
        currentWeight -= bridges.shift();
        const truck = truck_weights.shift();
        if(truck){
            if(currentWeight+truck <= weight){
                bridges.push(truck);
                currentWeight+=truck;
            }else{
                bridges.push(0);
                truck_weights.unshift(truck);
            }
        }else{
            if(currentWeight === 0){
                break;
            }
            bridges.push(0);
        }    
        
        
    }
    return second;
}