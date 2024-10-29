class Solution {
    public int solution(String[] order) {
        int result = 0;
        for (String ord: order) {
            if (ord.contains("americano") || ord.equals("anything")) {
                result += 4500;
            } else {
                result += 5000;
            }
        }
        return result;
    }
}