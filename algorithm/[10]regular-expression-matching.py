# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5: 
# 
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false 
#  Related Topics 字符串 动态规划 回溯算法

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatchTB(self, s: str, p: str) -> bool:
        """
        自顶向下
        :param s:
        :param p:
        :return:
        """
        mem = {}

        def dp(i, j):
            if (i, j) not in mem:
                if j == len(p):
                    ans = len(s) == i
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if len(p) - j >= 2 and p[j + 1] == '*':
                        ans = (first_match and dp(i + 1, j)) or dp(i, j + 2)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                mem[(i, j)] = ans
            return mem[(i, j)]

        return dp(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        """
        dp[i][j] = 表示s[0..i-1]到p[0..j-1]是否匹配
        {
            1. dp[i-1][j-1], if p[j-1] != '*'and p[j - 1] in {s[i - 1], '.'}
            2. dp[i][j-2],  pattern repeats for 0 times.
            3. dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), pattern repeat for at least 1 time.
        }
        :param s:
        :param p:
        :return:
        """

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = j > 1 and p[j - 1] == '*' and dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (p[j - 2] in {s[i - 1], '.'} and dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in {s[i - 1], '.'}
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().isMatch("aaabb", "a*c*b*"))
