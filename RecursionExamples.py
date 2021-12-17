class Solution:
    def longestCommonPrefix(self , strs):
        if len(strs)<=1:
            return ''
        elif len(strs) == 2:
            return self.lCPT(strs)
        else:
            return self.lCPT( [self.longestCommonPrefix(strs[:-1]), strs[-1] ] )

    def lCPT(self , strs):
        out = ''
        for i in range(min(len(strs[ 0 ]) , len(strs[ 1 ]))):
            if strs[ 0 ][ i ] == strs[ 1 ][ i ]:
                out += strs[ 0 ][ i ]
            else:
                return out