var lengthOfLongestSubstring = function(s) {
    let start = 0;
    let max = 0;
    let chars = {};
    for (let end = 0; end < s.length; end++) {
        let current = s[end]
        if (chars[current] !== undefined) {
            end = Math.max(chars[current] + 1, start + 1);
	    max = Math.max(end - start, max);
	    chars = {};
	}
        chars[current] = end;
    }
    return max;
};

console.log(lengthOfLongestSubstring("abcabcbb"));
// console.log(lengthOfLongestSubstring("bbbbb"));
// console.log(lengthOfLongestSubstring("pwwkew"));
