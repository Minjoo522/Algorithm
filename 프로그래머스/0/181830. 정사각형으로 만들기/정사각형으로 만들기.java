

class Solution {
    public int[][] solution(int[][] arr) {
        int x = arr[0].length;
        int y = arr.length;
        int n = x > y ? x : y;
        
        int[][] answer = new int[n][n];
        
        for (int i = 0; i < y; i++) {
            for (int j = 0; j < x; j++) {
                answer[i][j] = arr[i][j];
            }
        }
        return answer;
    }
}