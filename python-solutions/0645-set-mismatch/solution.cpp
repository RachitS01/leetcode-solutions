class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
     //x = duplicate, y = miising   
     long long n = nums.size();    

     long long Sum = n*(n+1)/2;
     long long Square_Sum = n*(n+1)*(2*n+1)/6;

     long long ActualSum = 0;
     long long ActualSquare_Sum = 0;
     for(long long x : nums){
        ActualSum += x;
        ActualSquare_Sum += x*x;
     }

     //x-y
     int Diff1 = ActualSum - Sum;
     //x^2 - y^2 
     int Diff2 = ActualSquare_Sum - Square_Sum;
     //-y^2 + x^2 by -y + x  = x + y
     int xplusy = Diff2/Diff1;

     //x + y - (x - y) == 2y  
     int missing = (xplusy - Diff1) / 2; // this is y
     int duplicate =  xplusy - missing;  // this is x + y - y = x
    
     return {static_cast<int>(duplicate), static_cast<int>(missing)} ;    
    }
};
