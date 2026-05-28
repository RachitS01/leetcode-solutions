class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {

        std::vector<int> freq(101,0);

        for (int n : nums){
            freq[n]++;
        }

        for (int i = 1; i < 101; i++){
            freq[i] = freq[i-1]+freq[i];
        }

        std::vector<int> output;
        for (int num: nums){
            if (num == 0){
                output.push_back(0);
            }
            else{
                output.push_back(freq[num-1]);
            }

        }
        return output;
    }
};
