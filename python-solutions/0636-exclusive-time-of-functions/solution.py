class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        stack = []
        prev_time = 0

        for log in logs:
            f_id, action, timestamp = log.split(':')
            f_id = int(f_id)
            timestamp = int(timestamp)

            if action == 'start':
                if stack:
                    ans[stack[-1]] = ans[stack[-1]] + timestamp - prev_time
                stack.append(f_id)
                prev_time = timestamp
            else:
                ending_fid = stack.pop()
                ans[ending_fid] += timestamp - prev_time + 1

                prev_time = timestamp + 1

        return ans  
             
             
