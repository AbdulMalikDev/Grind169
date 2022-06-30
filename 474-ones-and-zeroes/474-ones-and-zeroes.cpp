class Solution {
public:
    vector<vector<vector<int> > >dp;
int findMaxForm(vector<string>& strs, int m, int n) {        
	dp.resize(size(strs), vector<vector<int> >(m + 1, vector<int>(n + 1)));
	return helper(strs, m, n, 0);
}
int helper(vector<string>& strs, int m, int n, int idx){
	// base condition - all items covered, then stop further recusion
	if(idx == size(strs)) return 0; 
	// if the current case is already memoised - return it
	if(dp[idx][m][n]) return dp[idx][m][n];
	// count freqeuncy of zeros and ones in current string
	int zeros = count(begin(strs[idx]), end(strs[idx]), '0'), ones = size(strs[idx]) - zeros;
	dp[idx][m][n] = helper(strs, m, n, idx + 1); // case where current string is not chosen & move to next string
	// if current string can be chosen, find optimal between choosing it and leaving it
	if(m - zeros >= 0 && n - ones >= 0) 
		dp[idx][m][n] = max(dp[idx][m][n], 1 + helper(strs, m - zeros, n - ones, idx + 1));
	return dp[idx][m][n]; // finally the optimal answer will be returned
}
};