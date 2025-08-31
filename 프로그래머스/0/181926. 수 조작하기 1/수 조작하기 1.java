class Solution {
    public int solution(int n, String control) {
        int answer = n;
        char[] arr_char = control.toCharArray();
        
        for (char c : arr_char) {
            if (c == 'w') answer += 1;
            else if (c == 's') answer -= 1;
            else if (c == 'd') answer += 10;
            else answer -= 10;
        }
        
        return answer;
    }
}