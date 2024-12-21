import json
import functools

with open("input.txt", encoding="UTF-8") as file:
    data = json.load(file)

NON_OVERLAPPING_PATTERNS = [
    ['n', 's', 's', 'n'],
    ['n', 's', 's', 'e'],
    ['n', 'w', 's', 'e'],
    ['n', 'e', 's', 'w'],
    ['n', 'w', 'e', 'n'],
    ['n', 's', 'e', 'n'],
    ['n', 'w', 'w', 'n']
]
DIRECTION_SEQUENCE = ['n', 'w', 's', 'e', 'n', 'w', 's', 'e']
ROAD_PRIORITY = ['north', 'north-east', 'east', 'south-east', 'south', 'south-west', 'west', 'north-west']
ABBREVIATED_CODES = ['n', 'e', 's', 'w']
CURRENT_PRIORITY_LANES = []


def detect_collision(vehicle_a, vehicle_b):
    movement = [vehicle_a[1], vehicle_a[2], vehicle_b[1], vehicle_b[2]]
    for pattern in NON_OVERLAPPING_PATTERNS:
        temp_movement = movement[:]
        for _ in range(4):
            temp_movement[0] = DIRECTION_SEQUENCE[DIRECTION_SEQUENCE.index(temp_movement[0]) + 1]
            temp_movement[1] = DIRECTION_SEQUENCE[DIRECTION_SEQUENCE.index(temp_movement[1]) + 1]
            temp_movement[2] = DIRECTION_SEQUENCE[DIRECTION_SEQUENCE.index(temp_movement[2]) + 1]
            temp_movement[3] = DIRECTION_SEQUENCE[DIRECTION_SEQUENCE.index(temp_movement[3]) + 1]
            if temp_movement == pattern or (
                    temp_movement[:2] == pattern[2:] and temp_movement[2:] == pattern[:2]):
                return True
    return False


def evaluate_priority(vehicle_a, vehicle_b):
    global CURRENT_PRIORITY_LANES
    idx_a, from_a, to_a = vehicle_a
    idx_b, from_b, to_b = vehicle_b

    if from_a == from_b:
        return idx_a < idx_b

    if from_a in CURRENT_PRIORITY_LANES and from_b not in CURRENT_PRIORITY_LANES:
        return True
    if from_a not in CURRENT_PRIORITY_LANES and from_b in CURRENT_PRIORITY_LANES:
        return False

    if abs(DIRECTION_SEQUENCE.index(from_a) - DIRECTION_SEQUENCE.index(from_b)) == 1:
        return DIRECTION_SEQUENCE.index(from_a) > DIRECTION_SEQUENCE.index(from_b)
    return abs(DIRECTION_SEQUENCE.index(from_a) - DIRECTION_SEQUENCE.index(to_a)) < abs(
        DIRECTION_SEQUENCE.index(from_b) - DIRECTION_SEQUENCE.index(to_b))


def sort_by_rules(vehicle_a, vehicle_b):
    if detect_collision(vehicle_a, vehicle_b):
        return -1
    if evaluate_priority(vehicle_a, vehicle_b):
        return -1
    return 1


def road_ordering_comparator(road_a, road_b):
    return 1 if ROAD_PRIORITY.index(road_a) > ROAD_PRIORITY.index(road_b) else -1


def assign_vehicle_priorities(intersection_config, vehicle_list):
    global CURRENT_PRIORITY_LANES
    involved_roads = []
    CURRENT_PRIORITY_LANES = intersection_config.get("priority_lanes", [])

    for lane in CURRENT_PRIORITY_LANES:
        involved_roads.append(lane)

    normalized_vehicles = []
    for vehicle in vehicle_list:
        source = vehicle["lane"]
        destination = vehicle["direction"]
        involved_roads.extend([source, destination])

    involved_roads = sorted(set(involved_roads), key=functools.cmp_to_key(road_ordering_comparator))
    lane_mapping = {road: ABBREVIATED_CODES[i] for i, road in enumerate(involved_roads)}

    for vehicle in vehicle_list:
        vehicle_id = vehicle["vehicle_id"]
        entry_point = lane_mapping[vehicle["lane"]]
        exit_point = lane_mapping[vehicle["direction"]]
        normalized_vehicles.append([vehicle_id, entry_point, exit_point])

    normalized_vehicles.sort(key=functools.cmp_to_key(sort_by_rules))
    priorities = []
    current_priority = 1

    for idx in range(len(normalized_vehicles) - 1):
        priorities.append({"vehicle_id": normalized_vehicles[idx][0], "priority": current_priority})
        if not detect_collision(normalized_vehicles[idx], normalized_vehicles[idx + 1]):
            current_priority += 1

    priorities.append({"vehicle_id": normalized_vehicles[-1][0], "priority": current_priority})
    return sorted(priorities, key=lambda x: x["vehicle_id"])


def process_intersection(configuration):
    intersection = configuration["intersection"]
    vehicles = configuration["vehicles"]

    result_priorities = assign_vehicle_priorities(intersection, vehicles)

    return json.dumps({"order": result_priorities}, indent=2)


output = process_intersection(data)
print(output)
