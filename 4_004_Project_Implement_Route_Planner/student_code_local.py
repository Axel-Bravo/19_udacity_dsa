import heapq
from math import pow, sqrt
from collections import namedtuple

Cost = namedtuple('Cost', ['total', 'journey', 'to_goal'])  # (float, float)
Path = namedtuple('Path', ['cost', 'intersections', 'previous', 'frontier'])  # (Cost, [int, int ...], int, int)


class Map(object):
    """
    Temporary class simulating the real 'Map' class, due to problems opening the pickle
    No proper environment reproducibility
    """

    def __init__(self):
        self.intersections = None
        self.roads = None


def euclidean_distance(origin_point: [float, float], destination_point: [float, float]) -> float:
    """
    Given two points returns their euclidean distance
    :param origin_point: origin point, in the 2D cartesian space
    :param destination_point: destination point, in the 2D cartesian space
    :return: euclidean distance between the two points
    """

    return sqrt(pow((origin_point[0] - destination_point[0]), 2) + pow((origin_point[1] - destination_point[1]), 2))


def estimated_distance(path_frontier_point: [float, float], goal_point: [float, float]) -> float:
    """
    Estimates the distance between the current path frontier point and the goal. Accomplished the A* optimization
    requirement of having an estimating function that underestimates. As in a 2D-Cartesian space, the straight line is
    always the smallest possible distance between two points; guaranteeing the "underestimation" requirement
    :param path_frontier_point: path frontier point
    :param goal_point: goal point
    :return: estimated euclidean distance
    """
    return euclidean_distance(origin_point=path_frontier_point, destination_point=goal_point)


def update_path(map: Map, path: Path, new_frontier: int, goal: int) -> Path:
    """
    Given a path and a next point, updates the path
    :param map: map of the current 2D space
    :param path: current traversed path
    :param new_frontier: coordinates of next point to add to the path
    :param goal: coordinates of the goal intersection
    :return: path costs and intersections updated with new point
    """
    traversed_distance = euclidean_distance(origin_point=map.intersections[path.frontier],
                                            destination_point=map.intersections[new_frontier])
    new_path_cost_journey = path.cost.journey + traversed_distance
    new_path_cost_to_goal = estimated_distance(path_frontier_point=map.intersections[new_frontier],
                                               goal_point=map.intersections[goal])
    new_path_cost_total = new_path_cost_journey + new_path_cost_to_goal

    new_path_intersections = path.intersections + [new_frontier]

    new_path = Path(Cost(new_path_cost_total, new_path_cost_journey, new_path_cost_to_goal),
                    new_path_intersections, path.frontier, new_frontier)

    return new_path


def shortest_path(map: Map, start: int, goal: int) -> list:
    """
    Given a map and a start and end point, returns the shortest path, based on A* algorithm
    :param map: map of the current 2D space
    :param start: coordinates of the original intersection
    :param goal: coordinates of the goal intersection
    :return:
    """
    paths = list()
    path_goal_min_val = float('inf')
    path_goal_min = None

    # Check if already in goal
    if start == goal:
        return [start]

    # Initialize paths
    goal_initial_distance = estimated_distance(path_frontier_point=map.intersections[start],
                                               goal_point=map.intersections[goal])
    path = Path(Cost(goal_initial_distance, 0, goal_initial_distance), [start], start, start)
    heapq.heappush(paths, path)

    while len(paths) >= 1:
        nearest_frontier_path = heapq.heappop(paths)
        for neighbor_road in map.roads[nearest_frontier_path.frontier]:

            if neighbor_road == nearest_frontier_path.previous:  # Avoid returning to backwards
                continue
            else:  # Continue

                new_path = update_path(map=map, path=nearest_frontier_path, new_frontier=neighbor_road, goal=goal)

                if neighbor_road == goal:  # Reached destination with a path
                    if new_path.cost.total < path_goal_min_val:  # Better than previous path
                        path_goal_min_val = new_path.cost.total
                        path_goal_min = new_path.intersections
                    else:  # Reached destination, with higher cost -> disregard
                        pass
                else:
                    if path_goal_min is not None:  # Already found the goal with a path
                        if new_path.cost.total >= path_goal_min_val:  # Path not reached goal and already costly
                            pass
                        else:  # Cheaper path, keep exploring
                            heapq.heappush(paths, new_path)
                    else:  # Not yet found the goal, keep exploring
                        heapq.heappush(paths, new_path)

    if path_goal_min is not None:
        return path_goal_min
    else:
        return -1

#%% Test - Dev- Data Preparations
map_10 = Map()
map_10.intersections = {
    0: [0.7798606835438107, 0.6922727646627362],
    1: [0.7647837074641568, 0.3252670836724646],
    2: [0.7155217893995438, 0.20026498027300055],
    3: [0.7076566826610747, 0.3278339270610988],
    4: [0.8325506249953353, 0.02310946309985762],
    5: [0.49016747075266875, 0.5464878695400415],
    6: [0.8820353070895344, 0.6791919587749445],
    7: [0.46247219371675075, 0.6258061621642713],
    8: [0.11622158839385677, 0.11236327488812581],
    9: [0.1285377678230034, 0.3285840695698353]}

map_10.roads = [
    [7, 6, 5],
    [4, 3, 2],
    [4, 3, 1],
    [5, 4, 1, 2],
    [1, 2, 3],
    [7, 0, 3],
    [0],
    [0, 5],
    [9],
    [8]
]

#%%
result = shortest_path(map=map_10, start=6, goal=5)



