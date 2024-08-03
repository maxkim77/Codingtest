class Solution {
    public String solution(String my_string, String alp) {
        // Use the StringBuilder for efficient string concatenation
        StringBuilder answer = new StringBuilder();
        // Iterate through each character of my_string
        for(int i=0;i<my_string.length();i++){
            char currentChar = my_string.charAt(i);
        // Check if the current character matches 'alp'
            if(Character.toString(currentChar).equals(alp)){
        // Convert to uppercase and append to the result
                answer.append((char) (currentChar - 32));
        // Append the character unchanged
            }else{
                answer.append(currentChar);
            }
        }
        // Return the final string
        return answer.toString();
    }
}