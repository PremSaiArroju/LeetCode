/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    let n = ratings.length;
    let candies = new Array(n).fill(1);

    // Left to Right Pass
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }
    // Right to Left Pass
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
    }

    return candies.reduce((sum, c) => sum + c, 0);
};