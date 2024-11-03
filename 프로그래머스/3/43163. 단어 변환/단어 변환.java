/*
1. target이 word에 없으면 변환 불가
2. 큐 사용 -> 시작 단어와 단계 수를 추가해준다
3. 큐가 빌때까지
4. 큐에서 하나 빼준다
5. target이랑 동일하면 현재 변환 횟수 반환한다.
6. 현재 단어와 words 리스트 단어 비교하며 변환 가능한 단어 ㅌ마색한다
6-1. 방문한 적 없고, 변경이 가능해야 한다.
6-2. 그렇다면, 방문 처리하고
6-3. 큐에 추가한다.

변경이 가능한가? -> 두 단어가 한 글자만 다른지 확인한다.
1. for문을 돌면서 같은 위치의 char가 다르면 count++
2. 1보다 크면 return false
3. 1인지 확인하는 거 return

큐에 단어와 변환 단계를 같이 저장해야하기에 클래스를 써야한다.
*/
import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) {
            return 0;
        }
        
        Queue<WordNode> q = new LinkedList<>();
        q.add(new WordNode(begin, 0));
        
        boolean[] visited = new boolean[words.length];
        
        while (!q.isEmpty()) {
            WordNode current = q.poll();
            
            if (current.word.equals(target)) {
                return current.step;
            }
            
            for (int i = 0; i < words.length; i++) {
                if (!visited[i] && canTransform(current.word, words[i])) {
                    visited[i] = true;
                    q.add(new WordNode(words[i], current.step + 1));
                }
            }
        }
        
        return 0;
    }
    
    private boolean canTransform(String begin, String target) {
        int diffCount = 0;
        
        for (int i = 0; i < begin.length(); i++) {
            if (begin.charAt(i) != target.charAt(i)) {
                diffCount++;
            }
            
            if (diffCount > 2) {
                return false;
            }
        }
        
        return diffCount == 1;
    }
}

class WordNode {
    String word;
    int step;
    
    WordNode(String word, int step) {
        this.word = word;
        this.step = step;
    }
}