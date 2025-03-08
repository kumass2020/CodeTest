import math

def solution(fees, records):
    answer = []
    
    car_numbers = {}
    costs = {}
    
    for record in records:
        time, car_number, event = record.split(" ")
        time_min = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
        # total_time = 0
        
        if event == "IN":
            if car_numbers.get(car_number):
                _, _, total_time = car_numbers[car_number]
            else:
                total_time = 0
            pass
        elif event == "OUT":
            in_time, _, total_time = car_numbers[car_number]
            total_time = total_time + time_min - in_time
        
        car_numbers[car_number] = [time_min, event, total_time]
    
    for key, value in car_numbers.items():
        car_number = key
        in_time, _, total_time = value
        
        if value[1] == "IN":
            time_min = (23 * 60 + 59)
            total_time = total_time + time_min - in_time
                
            car_numbers[car_number] = [time_min, event, total_time]
            # if time_min - in_time <= fees[0]:
            #     cost = fees[1]
            # else:
            #     cost = fees[1] + math.ceil((time_min - in_time - fees[0]) / fees[2]) * fees[3]
            # if costs.get(car_number):
            #     costs[car_number] += cost
            # else:
            #     costs[car_number] = cost
            
    for key, value in car_numbers.items():
        car_number = key
        in_time, _, total_time = value
        
        if total_time <= fees[0]:
            cost = fees[1]
        else:
            cost = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]

        if costs.get(car_number):
            costs[car_number] += cost
        else:
            costs[car_number] = cost
                
        
    sorted_car_numbers = sorted(costs.keys())
    for num in sorted_car_numbers:
        answer.append(costs[num])
    
    return answer