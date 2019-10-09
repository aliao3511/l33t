var lengthOfLongestSubstring = function(s) {
    let start, end = 0;
    let chars = {};
    for (let end = 0; end < s.length; end++) {
        let current = s[end]
        console.log(`current: ${current}`);
	console.log(chars);
        if (chars[current] !== undefined) {
	    console.log(`repeat! ${chars[current]}`)
            end = Math.max(chars[current] + 1, start + 1);
	    console.log(chars[current] + 1)
	    console.log(start + 1)
	    chars = {};
	    console.log(`newend: ${end}`);
	}
        chars[current] = end;
	console.log(chars)
	console.log('\n');
    }
    return end - start;
};

console.log(lengthOfLongestSubstring("abcabcbb"));
// console.log(lengthOfLongestSubstring("bbbbb"));
// console.log(lengthOfLongestSubstring("pwwkew"));
