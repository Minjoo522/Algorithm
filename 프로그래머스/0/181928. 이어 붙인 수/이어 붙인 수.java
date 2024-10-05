import java.lang.StringBuilder;

class Solution {
    public int solution(int[] num_list) {
        StringBuilder sb_odd = new StringBuilder();
        StringBuilder sb_even = new StringBuilder();
        for (int num: num_list) {
            if (num % 2 == 0) {
                sb_even.append(num);
            } else {
                sb_odd.append(num);
            }
        }
        return Integer.parseInt(sb_odd.toString()) + Integer.parseInt(sb_even.toString());
    }
}