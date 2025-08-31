class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        
        for (int i = 0; i < numLog.length - 1; i++) {
            int dist = numLog[i + 1] - numLog[i];
            
            if (dist == 1) answer += "w";
            else if (dist == -1) answer += "s";
            else if (dist == 10) answer += "d";
            else answer += "a";
        }
            
        return answer;
    }
}