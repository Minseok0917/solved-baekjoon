function solution(num_list) {
    return (num_list.sort((a,b) => a-b).splice(0,5),num_list)
    
}