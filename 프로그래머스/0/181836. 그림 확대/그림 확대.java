import java.util.*;
import java.lang.*;

class Solution {
    public String[] solution(String[] picture, int k) {
        // 가로 : String길이의 k배
        // 세로 : 배열 길이의 k배
        // 글자 하나 가져오기 -> 세로 for 문, 가로 for 문
        // 데이터 저장하기 -> String버퍼에 한 줄씩 저장 -> 똑같은 걸 k 번 넣으면 된다!
        // 한 글자가 가로 세로 둘 다 늘어나야 함
        List<String> result = new ArrayList<>();
        String[] tmp = new String[picture.length];
        for (int i = 0; i < picture.length; i++) {
            StringBuilder sb = new StringBuilder();
            String curr = picture[i];
            for (char ch: curr.toCharArray()) {
                sb.append(String.valueOf(ch).repeat(k));
            }
            tmp[i] = sb.toString();
        }
        
        for (int i = 0; i < tmp.length; i++) {
            for (int j = 0; j < k; j++) {
                result.add(tmp[i]);
            }
        }
        
        return result.toArray(String[]::new);
    }
}