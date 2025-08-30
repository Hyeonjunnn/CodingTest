import java.lang.String;

class Solution {
    public int solution(String my_string, String is_prefix) {        
        int answer = 0;
        if (my_string.matches(is_prefix+"(.*)") == true) {
            answer = 1;
        }
        
        return answer;
    }
}