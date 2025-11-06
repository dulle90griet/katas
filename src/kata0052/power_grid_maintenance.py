def find_lowest_connected_id(self, connection_map: list[set], is_online: list[bool], target: int) -> int:
    # initialize lowest_id variable to infinity
    lowest_id = float('inf')
    # create stack containing the current node
    station_stack = [target]
    # create empty visited node hashmap
    visited = {target}

    while station_stack:
        # pop the top node from the stack - make it our current node
        cur_station = station_stack.pop()
        # check whether lowest_id or the node's id is lower. update lowest_id accordingly
        if is_online[cur_station-1]:
            lowest_id = min(lowest_id, cur_station)

        # traverse the node's list of connections
        for connection in connection_map[cur_station-1]:
            # for every connection not already visited, add it to the stack and the visited list
            if connection not in visited:
                visited.add(connection)
                station_stack.append(connection)

    # when the stack is empty, return lowest_id
    return -1 if lowest_id == float('inf') else lowest_id


def process_queries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
    # keep list of online/offline station statuses
    is_online = [True for station in range(c)]
    station_map = [set() for station in range(c)]
    # make empty response list
    responses = []

    # convert connection list to map of nodes with reciprocal connections
    for connection in connections:
        station_map[connection[0]-1].add(connection[1])
        station_map[connection[1]-1].add(connection[0])
    
    # traverse list of queries
    for query in queries:
        if query[0] == 1:
            # if query[1] is 1, check the station's status
            if is_online[query[1]-1]:
                # if the station is online, add its id to the response list
                responses.append(query[1])
            else:
                # if the station is online, begin traversing the grid
                # add the returned lowest connected id to the response list
                responses.append(self.find_lowest_connected_id(station_map, is_online, query[1]))
        # if query[0] is 2, take the station offline
        elif query[0] == 2:
            is_online[query[1]-1] = False
    
    # when the list of queries is exhausted, return the response list
    return responses