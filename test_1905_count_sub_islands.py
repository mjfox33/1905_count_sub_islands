from code_1905_count_sub_islands import Solution

def test_example_1():
    s = Solution()
    g1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    g2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    output = 3
    assert s.countSubIslands(g1, g2) == output