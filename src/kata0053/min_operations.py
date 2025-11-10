def min_operations(nums: list[int]) -> int:
    def count_ops(start, end):
        op_count = 0
        base_positions = []
        span_min = float('inf')

        for i in range(start, end):
            if nums[i] < span_min:
                span_min = nums[i]
                base_positions = [start-1, i]
            elif nums[i] == span_min:
                base_positions.append(i)
        base_positions.append(end)

        if span_min > 0:
            op_count += 1
            
        for p in range(1, len(base_positions)):
            span_start = base_positions[p-1] + 1
            span_end = base_positions[p]

            if span_end - span_start == 1:
                op_count += 1
            elif span_end - span_start > 1:
                op_count += count_ops(span_start, span_end)
        
        return op_count
    
    return count_ops(0, len(nums))