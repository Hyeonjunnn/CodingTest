import java.util.ArrayList;

class Solution {
    public Integer[] solution(int n) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        
        while(true) {
            arrayList.add(n);
            if (n == 1) break;
            
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = (3 * n + 1);
            }
            
        }
        
        Integer[] answer = arrayList.toArray(new Integer[arrayList.size()]);
        
        return answer;
    }
}