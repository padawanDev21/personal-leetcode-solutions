class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # These 2 variables store l1 and l2 values in string.
        l1_val_str = ""
        l2_val_str = ""
        
        # Inserting each node values to the variable l1_val_str above.
        while l1:
            l1_val_str += str(l1.val)
            l1 = l1.next
        
        # Inserting each node values to the variable l2_val_str above.
        while l2:
            l2_val_str += str(l2.val)
            l2 = l2.next
        
        # Reversing values to form the actual numbers.
        l1_val_str = l1_val_str[::-1]
        l2_val_str = l2_val_str[::-1]
        
        # Adding the two numbers to get the actual result.
        val_res = str(int(l1_val_str) + int(l2_val_str))

        # Reversing the addition result to match the result's pattern.
        val_res = val_res[::-1]
        
        # Create the result node by looping the val_res variable's value (the result string).
        res_node = ListNode(val_res[0], None)
        ans = res_node
        for i in range(1, len(val_res)):
            res_node.next = ListNode(val_res[i], None)
            res_node = res_node.next
        
        return ans
    