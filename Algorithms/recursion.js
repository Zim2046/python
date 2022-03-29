function sumArr(nums, i = 0){
    if(i == nums.length){
        return 0;
    }
    return nums[i] + sumArr(nums, i + 1)
}
var nums1 = [1,2,3]

sumArr(nums1)