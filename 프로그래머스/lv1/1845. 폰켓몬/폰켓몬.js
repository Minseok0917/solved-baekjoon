function solution(nums) {
    const m = nums.length/2;
    const numSet = [...new Set(nums)]
    const length = numSet.length;
    return length >= m ? m : m-(m-length);
}