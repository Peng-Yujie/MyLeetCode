/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode doubleIt(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode temp = dummy;
        while (temp.next != null) {
            temp.val = (temp.val * 2) % 10 + (temp.next.val * 2) / 10;
            temp = temp.next;
        }
        temp.val = (temp.val * 2) % 10;
        return dummy.val == 0 ? head : dummy;
    }
}