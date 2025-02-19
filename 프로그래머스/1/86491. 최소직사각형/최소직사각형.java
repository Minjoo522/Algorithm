import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        // 명함의 가로, 세로 중 큰 값을 항상 가로로, 작은 값을 항상 세로로 둔다
        int maxWidth = 0;
        int maxHeight = 0;
        
        for (int[] size: sizes) {
            int width = Math.max(size[0], size[1]);
            int height = Math.min(size[0], size[1]);
            
            maxWidth = Math.max(maxWidth, width);
            maxHeight = Math.max(maxHeight, height);
        }
        
        return maxWidth * maxHeight;
    }
}