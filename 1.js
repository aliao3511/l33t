/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function (nums, target) {
    const indices = {};
    for (let i = 0; i < nums.length; i++) {
        if (indices[target - nums[i]] >= 0) {
            return [indices[target - nums[i]], i];
        }
        indices[nums[i]] = i;
    }
};

// time complexity: 
// O(N) - iterate through list, getting and setting in an object is O(1)