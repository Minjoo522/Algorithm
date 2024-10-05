import java.lang.Math;

class Solution {
    public int solution(int[] num_list) {
        int multiply = 1;
        int sum_num = 0;
        for (int num: num_list) {
            multiply *= num;
            sum_num += num;
        }
        return multiply < Math.pow(sum_num, 2) ? 1 : 0;
    }
}