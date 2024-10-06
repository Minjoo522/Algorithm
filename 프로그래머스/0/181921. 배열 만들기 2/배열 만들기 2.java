import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> result = new ArrayList<>();
        
        for (int i = 1; i < 64; i++) { // 2의 6승
            int num = Integer.parseInt(Integer.toBinaryString(i)) * 5;
            // 이진수(Binary) 문자열로 변환 후 5 곱해서 1을 5로 만들기
            if (l <= num && num <= r) {
                result.add(num);
            }
        }
        return result.isEmpty() ? new int[]{-1} : result.stream().mapToInt(i -> i).toArray();
    }
}