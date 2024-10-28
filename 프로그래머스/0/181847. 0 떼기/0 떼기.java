class Solution {
    public String solution(String n_str) {
        while (true) {
            if (n_str.startsWith("0")) {
                n_str = n_str.replaceFirst("0", "");
            } else {
                break;
            }
        }
        return n_str;
    }
}