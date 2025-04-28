/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    let res = 0;
    for (let i = 0; i < 32; i++) {
        res = res << 1;        // Shift res left
        res += (n & 1);        // Add the least significant bit of n to res
        n = n >>> 1;           // Shift n to the right (unsigned shift)
    }
    return res >>> 0;          // Ensure the result is unsigned
};