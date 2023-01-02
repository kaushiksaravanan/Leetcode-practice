class Solution {
    public boolean detectCapitalUse(String word) {
        int up=0;
        int lo=0;
        // Char[] word=str.toCharArray();
        for(int i=0;i<word.length();i++)
        {
            if(Character.isUpperCase(word.charAt(i)))
            {
                up+=1;
            }
            else
            {lo+=1;
            }
            
        }
        if(lo==word.length() || up==word.length())
            return true;
        if(up==1 && lo+1==word.length()&&Character.isUpperCase(word.charAt(0)))
            return true;
        return false;
        
        
    }
}