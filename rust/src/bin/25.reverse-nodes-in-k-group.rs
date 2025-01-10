/*
 * @lc app=leetcode id=25 lang=rust
 *
 * [25] Reverse Nodes in k-Group
 */

// @lc code=start
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {

        // grab head walk down list reversing the link directions
        // at the kth element we jump back to "head" and link that to the next "head"
        // the kth element was pointing to.
        // repeat

        let mut prev_kth_head: Option<Box<ListNode>> = None;
        let mut kth_head: Box<ListNode> = head.unwrap().as_mut();
        let mut k_index: i32 = 0;
        let mut last: Box<ListNode>;
        let mut new_head: Option<Box<ListNode>> = None;
        let found_head: bool = false;
        let mut node: Option<Box<ListNode>> = head;


        last = kth_head;
        node = last.next;
        k_index += 1;

        while (node.is_some())
        {
            let current = node.unwrap().as_mut();
            k_index += 1;
            if (k_index >= k){
                // if this is the first this node will be the new head of the 
                if (!found_head){
                    new_head = node;
                    found_head = true;
                }
                
                // point prev kth head to current node (will be start of current chain)
                if (prev_kth_head.is_some()){
                    prev_kth_head.unwrap().next = node;
                }
                prev_kth_head = Some(kth_head);

                // link the current kth head to next node - might need to update if chain ends
                k_index = 0;
                kth_head = current;
            }
            else if( k_index == 1){
                last = current;
            }
            else{
                current.next = Some(last);
                last = current;
            }

            node = current.next;
        }

        return new_head;
        
    }
}
// @lc code=end

