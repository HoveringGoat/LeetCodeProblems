public class Solution
{
    public int RomanToInt(string s)
    {
        // roman numerals are in ascending order.
        // if the previous number is greater it means subtract the smaller from the greater. 

        int lastValues = 0;
        char lastChar = s[0];
        int finalValue = 0;

        foreach (char c in s){
            var value = GetValue(c);
            if (lastChar == c)
            {
                lastValues += value;
            }
            else
            {
                lastChar = c;
                if (value > lastValues)
                {
                    // subtract
                    lastValues = value - lastValues;
                }
                else
                {
                    finalValue += lastValues;
                    lastValues = value;
                }
            }
        }
                    
        finalValue += lastValues;
        return finalValue;
    }

    int GetValue(char c)
    {
        if(c == 'I'){
            return 1;
        }
        if(c == 'V'){
            return 5;
        }
        if(c == 'X'){
            return 10;
        }
        if(c == 'L'){
            return 50;
        }
        if(c == 'C'){
            return 100;
        }
        if(c == 'D'){
            return 500;
        }
        if(c == 'M'){
            return 1000;
        }
        return 0;
    }
}