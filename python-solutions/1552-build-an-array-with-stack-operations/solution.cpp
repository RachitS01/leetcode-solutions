class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> output;
        int target_idx = 0;

        for(int i = 1; i <= n; i++){
            output.push_back("Push");

            if( i == target[target_idx]){
                target_idx++;
            } else {
                output.push_back("Pop");
            }

            if (target_idx == target.size()){
                break;
            } 
        }       
    return output; 
    }     
};
