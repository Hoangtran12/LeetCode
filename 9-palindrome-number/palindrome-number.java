public class Solution {
    public boolean isPalindrome(int x) {
        int n = x;
        long rev = 0;
        while (x > 0) {
            rev = (rev * 10) + (x % 10);
            x /= 10;
        }
        if (rev == n) return true;
        return false;
    }
}