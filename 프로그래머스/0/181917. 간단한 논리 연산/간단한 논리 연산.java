class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean a = x1 == x2 ? x1 : true;
        boolean b = x3 == x4 ? x3 : true;
        return a == b ? a : false;
    }
}