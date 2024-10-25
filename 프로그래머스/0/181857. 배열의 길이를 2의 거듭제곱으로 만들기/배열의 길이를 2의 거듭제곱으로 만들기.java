// 2로 나누기를 반복하여 마지막에 1이 되는지 확인
// 가장 가까운 2의 거듭제곱을 구한다.

class Solution {
    public int[] solution(int[] arr) {
        int arrSize = arr.length;
        if (isPowerOfTwo(arrSize)) {
            return arr;
        }
        
        int minPowTwo = 1;
        while (minPowTwo < arrSize) {
            minPowTwo *= 2;
        }
        
        int[] result = new int[minPowTwo];
        for (int i = 0; i < arrSize; i++) {
            result[i] = arr[i];
        }
        
        return result;
    }
    
    private static boolean isPowerOfTwo(int num) {
        if (num < 1) {
            return false;
        }
        
        while (num > 1) {
            if (num % 2 == 0) {
                return false;
            }
            num /= 2;
        }
        return true;
    }
}