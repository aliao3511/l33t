


// linear solution: O(M + N)

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    merged = new Array(nums1.length + nums2.length);
    idx1 = 0;
    idx2 = 0;

    for (let i = 0; i < merged.length; i++) {
        if (idx1 < nums1.length && idx2 < nums2.length) {
            if (nums1[idx1] <= nums2[idx2]) {
                merged[i] = nums1[idx1++];
            } else {
                merged[i] = nums2[idx2++];
            }
        } else if (idx1 >= nums1.length) {
            merged[i] = nums2[idx2++];
        } else {
            merged[i] = nums1[idx1++];
        }
    }
    length = merged.length;
    return length % 2 === 0 ? (merged[length/2] + merged[length/2 - 1]) / 2 : merged[Math.floor(length/2)];
};