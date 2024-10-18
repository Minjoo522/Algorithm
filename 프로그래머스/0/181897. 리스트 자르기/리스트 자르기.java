class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        
        if (n == 1) {
            int[] result = new int[b + 1];
            for (int i = 0; i <= b; i++) {
                result[i] = num_list[i];
            }
            return result;
        }
        if (n == 2) {
            int[] result = new int[num_list.length - a];
            for (int i = a, j = 0; i < num_list.length; i++, j++) {
                result[j] = num_list[i];
            }
            return result;
        }
        if (n == 3) {
            int[] result = new int[b - a + 1];
            for (int i = a, j = 0; i <= b; i++, j++) {
                result[j] = num_list[i];
            }
            return result;
        }
        int[] result = new int[(b - a) / c + 1];
        for (int i = a, j = 0; i <= b; i += c, j++) {
            result[j] = num_list[i];
        }
        return result;
    }
}