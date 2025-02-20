from datetime import datetime, timedelta
from collections import deque

def solution(plans):
    answer = []
    
    sorted_plans = sorted(plans, key=lambda x: datetime.strptime(x[1], "%H:%M"))
    stack = deque()
    
    for i, plan in enumerate(sorted_plans):
        name = plan[0]
        start_time = datetime.strptime(plan[1], "%H:%M")
        playtime = timedelta(minutes=int(plan[2]))
        
        new_time = start_time + playtime
        
        
        if i != len(sorted_plans)-1:
            next_start_time = datetime.strptime(sorted_plans[i+1][1], "%H:%M")
        
            # 진행하다가 다음 과제가 먼저 오면 멈추고 그 다음 과제를 시작
            if new_time > next_start_time:
                elapsed_time = next_start_time - start_time
                remaining_time = playtime - elapsed_time

                stack.append((name, remaining_time))
            else:
                answer.append(name)
            
            # 다음 과제까지 여유 시간이 생겼을 때
            if stack and new_time < next_start_time:
                while stack:
                    new_plan = stack.pop()
                    name = new_plan[0]
                    playtime = new_plan[1]
                    start_time = new_time
                    
                    new_time = start_time + playtime
                    
                    if new_time > next_start_time:
                        elapsed_time = next_start_time - start_time
                        remaining_time = playtime - elapsed_time

                        stack.append((name, remaining_time))
                        break
                    else:
                        answer.append(name)
        else:
            answer.append(name)
            
            while stack:
                new_plan = stack.pop()
                name = new_plan[0]
                playtime = new_plan[1]
                start_time = new_time
                
                answer.append(name)
                        
            
    
    return answer