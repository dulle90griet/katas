def find_lowest_connected_id(connections: list[list[int]]) -> int:
    pass

def processQueries(c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
    is_online = [True for station in range(c)]

# convert connection list to map of nodes with reciprocal connections
# keep list of online/offline station statuses
# make empty response list
# traverse list of queries
# if query[0] is 2, take the station offline
# if query[1] is 1, check the station's status
# if the station is online, return its id
# if the station is online, begin traversing the grid
# create empty visited node hashmap
# initialize lowest_id variable to 0
# create stack containing the current node
# pop the top node from the stack - make it our current node
# check whether lowest_id or the node's id is lower. update lowest_id accordingly
# traverse the node's list of connections
# for every connection not already visited, add it to the stack and the visited list
# when the stack is empty, return lowest_id
# when the list of queries is exhausted, return the response list