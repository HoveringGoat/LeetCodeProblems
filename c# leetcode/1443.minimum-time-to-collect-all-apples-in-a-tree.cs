/*
 * @lc app=leetcode id=1443 lang=csharp
 *
 * [1443] Minimum Time to Collect All Apples in a Tree
 */

// @lc code=start
using System.Collections.Generic;
using System.Data;
using System.Reflection.Metadata.Ecma335;
public class Solution
{
    public int MinTime(int n, int[][] edges, IList<bool> hasApple)
    {
        var map = buildAdjDict(edges);
        int timePicking = pickApples(0, map, hasApple, 0);
        return timePicking;
    }

    public Dictionary<int, List<int>> buildAdjDict(int[][] edges)
    {
        Dictionary<int, List<int>> map = new Dictionary<int, List<int>>();
        
        foreach (var edge in edges){
            if (map.ContainsKey(edge[0]))
            {
                map[edge[0]].Add(edge[1]);
            }
            else
            {
                map[edge[0]] = new List<int>{edge[1]};
            }
            
            if (map.ContainsKey(edge[1]))
            {
                map[edge[1]].Add(edge[0]);
            }
            else
            {
                map[edge[1]] = new List<int>{edge[0]};
            }
        }
        return map;
    }


    // find leaf nodes, if apple add +2 to the time count
    public int pickApples(int index, Dictionary<int, List<int>> map, IList<bool> hasApple, int lastIndex)
    {
        var timePicking = 0;
        if (map.ContainsKey(index)){
            foreach (var n in map[index])
            {
                // dont reverse back up
                if (lastIndex == n){
                    continue;
                }
                timePicking += pickApples(n, map, hasApple, index);
            }
        }
        
        // count this node if we either have an apple here or picked one downstream
        if (index != 0)
        {
            if (timePicking > 0 || hasApple[index])
            {
                timePicking += 2;
            }
        }
        return timePicking;
    }
}

// @lc code=end

