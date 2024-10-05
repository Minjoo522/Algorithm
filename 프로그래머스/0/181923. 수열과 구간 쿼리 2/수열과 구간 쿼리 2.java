class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            int current = 987654321;
            int s = queries[i][0];
            int e = queries[i][1];
            int k = queries[i][2];
            
            for (int j = s; j <= e; j++) {
                int num = arr[j];
                if (num > k && num < current) {
                    current = num;
                }
            }
            answer[i] = current == 987654321 ? -1 : current;
        }
        return answer;
    }
}