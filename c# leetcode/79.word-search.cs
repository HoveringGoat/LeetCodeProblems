/*
 * @lc app=leetcode id=79 lang=csharp
 *
 * [79] Word Search
 */

// @lc code=start
using System.Net.WebSockets;
using Microsoft.VisualBasic;

public partial class Solution
{
    public bool Exist(char[][] board, string word)
    {
        for(var i = 0; i < board[0].Length; i++)
        {
            for(var j = 0; j < board.Length; j++)
            {
                Console.WriteLine($"({i},{j}) found char: {board[j][i]} - word: {word}");
                if (board[j][i] == word[0]){
                    // test if the rest of the word follows
                    char[][] newBoard = board.Clone() as char[][];
                    newBoard[j][i] = ' ';
                    if (ContainsSubWord(newBoard, word.Substring(1), i, j ))
                    {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    public bool ContainsSubWord(char[][] board, string word, int xPosition, int yPosition)
    {
        if (word == "")
        {
            return true;
        }

        Console.WriteLine($"({xPosition},{yPosition}) remaining word: {word}");

        // look in every adjacent cell for the new first letter in the remaining word. If we find it continue if we dont fail

        for (int i = 0; i < 4; i++){
            
            var x = xPosition;
            var y = yPosition;
            if (i == 0)
            {
                x += 1; 
            }
            if (i == 1)
            {
                x -= 1; 
            }
            if (i == 2)
            {
                y += 1; 
            }
            if (i == 3)
            {
                y -= 1; 
            }

            if (x >= board[0].Length || x < 0 || y >= board.Length || y < 0){
                continue;
            }
            
            Console.WriteLine($"({x},{y}) found char: {board[y][x]} - word: {word}");
            if ((board[y][x]) == word[0])
            {
                // test if the rest of the word follows
                
                char[][] newBoard = board.Clone() as char[][]; // not duplicating correctly. idgaf
                newBoard[y][x] = ' ';
                if (ContainsSubWord(newBoard, word.Substring(1), x, y))
                {
                    return true;
                }
            }
        }
 
    
        Console.WriteLine("fail");
        return false;
    }
}
// @lc code=end

