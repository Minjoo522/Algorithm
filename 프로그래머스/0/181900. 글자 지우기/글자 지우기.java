class Solution {
    public String solution(String my_string, int[] indices) {
        String[] result = my_string.split("");
        for (int i = 0; i < indices.length; i++) {
            result[indices[i]] = "";
        }
        return String.join("", result);
    }
}