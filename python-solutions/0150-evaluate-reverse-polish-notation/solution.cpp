class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<long> stack; // Using long prevents potential 32-bit overflow during intermediate steps
        
        for (const string& token : tokens) {
            // Check if the token is an operator. 
            // Checking size == 1 ensures we don't accidentally treat negative numbers like "-11" as subtraction!
            if (token.size() == 1 && string("+-*/").find(token) != string::npos) {
                long num2 = stack.back(); 
                stack.pop_back();
                
                long num1 = stack.back();
                stack.pop_back();
                
                if (token == "+") stack.push_back(num1 + num2);
                else if (token == "-") stack.push_back(num1 - num2);
                else if (token == "*") stack.push_back(num1 * num2);
                else stack.push_back(num1 / num2); // C++ naturally truncates toward zero!
            } 
            else {
                // It's a number. Convert it to a long and push it.
                stack.push_back(stol(token));
            }
        }
        
        return stack.back();
    }
};
