/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let filteredstr = []
    for (let i = 0; i < s.length; i++){
        let char = s[i].toLowerCase();
        if((char >= 'a' && char <= 'z') || (char >= '0' && char <= '9')){
            filteredstr.push(char);
        }   
    }
    let left = 0, right  = filteredstr.length - 1;
    while (left < right){
        if (filteredstr[left] !== filteredstr[right]){
            return false;
        }
        left++;
        right--;
    }
    return true ;
};