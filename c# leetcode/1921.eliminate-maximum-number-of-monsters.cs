namespace c__leetcode
{
    public class Solution
    {
        public int EliminateMaximum(int[] dist, int[] speed)
        {
            int[] turns = TurnsToImpact(dist, speed);
            Array.Sort(turns);

            // we can nuke one monster per "turn" so i is turns
            // the array is sorted so if the number of turns is every less
            // than its index then it is unstoppable.
            for (int i = 0; i < turns.Length; i++)
            {
                if (turns[i] <= i)
                {
                    // i is 0 indexed so we can just return;
                    return i;
                }
            }

            // cool we killed em all.
            return turns.Length;
        }

        int[] TurnsToImpact(int[] dist, int[] speed)
        {
            int[] turns = new int[dist.Length];

            for (int i = 0; i < dist.Length; i++)
            {
                // convert to number of turns until city destroyed. 0 means city is rekt. Since we round up.
                turns[i] = (int)(Math.Ceiling(dist[i] / (double)speed[i]) + .5);
            }

            return turns;
        }
    }
}