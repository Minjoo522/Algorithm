class Solution {
    public int solution(int[] arr) {
        int count = -1;
        int[] nextArr = new int[arr.length];

        while(!isEqual(arr, nextArr)){
            for(int i=0; i<arr.length; i++){
                if(arr[i] >= 50 && arr[i] % 2 == 0){
                    nextArr[i] = arr[i] / 2;
                } else if(arr[i] < 50 && arr[i] % 2 != 0){
                    nextArr[i] = arr[i] * 2 + 1;
                }
            }
            count++;
            arr = nextArr;
            nextArr = new int[arr.length];
        }
        return count;
    }

    private boolean isEqual(int[] arr1,int[] arr2){
        if(arr1.length != arr2.length){
            return false;
        }

        for(int i = 0; i < arr1.length; i++){
           if(arr1[i] != arr2[i]){
               return false;
           }
        }
        return true;
    }
}