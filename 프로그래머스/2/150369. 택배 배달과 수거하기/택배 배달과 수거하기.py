def solution(cap, n, deliveries, pickups):
    distance = 0
    last_deliver = n - 1  # last index with a nonzero delivery
    last_pickup = n - 1   # last index with a nonzero pickup

    # Update the pointer to the last nonzero element.
    def update_last(arr, idx):
        while idx >= 0 and arr[idx] == 0:
            idx -= 1
        return idx

    last_deliver = update_last(deliveries, last_deliver)
    last_pickup = update_last(pickups, last_pickup)

    while last_deliver >= 0 or last_pickup >= 0:
        # The farthest house to visit in this trip:
        farthest = max(last_deliver, last_pickup)
        # Go to farthest house and come back.
        distance += (farthest + 1) * 2

        # Process deliveries from the farthest house backward.
        cap_left = cap
        for i in range(last_deliver, -1, -1):
            if deliveries[i] > 0:
                if deliveries[i] > cap_left:
                    deliveries[i] -= cap_left
                    cap_left = 0
                    break
                else:
                    cap_left -= deliveries[i]
                    deliveries[i] = 0
        last_deliver = update_last(deliveries, last_deliver)

        # Process pickups from the farthest house backward.
        cap_left = cap
        for i in range(last_pickup, -1, -1):
            if pickups[i] > 0:
                if pickups[i] > cap_left:
                    pickups[i] -= cap_left
                    cap_left = 0
                    break
                else:
                    cap_left -= pickups[i]
                    pickups[i] = 0
        last_pickup = update_last(pickups, last_pickup)

    return distance