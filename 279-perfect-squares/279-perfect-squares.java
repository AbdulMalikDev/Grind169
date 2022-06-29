class Solution {
int[] mem;
    public int numSquares(int n) {
        mem = new int[n+1];
        Arrays.fill(mem, -1);
        
        return dfs(n);
    }
    
    int dfs(int n) {
        if (n < 0) return Integer.MAX_VALUE;
        if (n == 0) return 0;
        if (mem[n] != -1) return mem[n];
        int min = n+1;
        for (int i=1;i*i<=n;i++) {
            min = Math.min(dfs(n-(i*i)), min);
        }
        mem[n] = min+1;
        return min+1;
    }
}