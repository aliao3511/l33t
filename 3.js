var lengthOfLongestSubstring = function (s) {
    let start = 0;
    let max = 0;
    let chars = {};
    for (let end = 0; end < s.length; end++) {
        let current = s[end];
        if (chars[current] !== undefined) {
            start = Math.max(chars[current] + 1, start);
        }
        max = Math.max(end - start + 1, max);
        chars[current] = end;
    }
    return max;
};