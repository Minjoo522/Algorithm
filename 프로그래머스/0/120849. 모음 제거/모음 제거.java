class Solution {
    public String solution(String my_string) {
        String vowels = "aeiou";
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < my_string.length(); i++) {
            char current = my_string.charAt(i);
            if (!vowels.contains(String.valueOf(current))) {
                sb.append(current);
            }
        }
        
        return sb.toString();
    }
}