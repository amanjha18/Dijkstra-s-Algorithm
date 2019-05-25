graph = {

'0':{'1':4, '7':8},
'1':{'2':8},
'2':{'8':2, "3":7},
'3':{'4':9, "5":14},
'4':{"3":9, "5":10},
'5':{'4':10},
'6':{"5":2},
'7':{"6":1},
'8':{"2":2, "6":6}
}

def dijkstra(graph,start,end):

    short_distance = {} #dictionary to record the cost to reach to node. We will constantly update this dictionary as we move along the graph.
    track_predecessor = {} #dictionary to keep track of path that led to that node.
    remainingNodes = graph #to iterate all nodes.
    infinity = 5000 #infinity can be considered a very large number
    track_path = [] #dictionary to record as we trace back our journey

# Initially we want to assign 0 as the cost to reach to source node and infinity as cost to all other nodes

    for node in remainingNodes:
        short_distance[node] = infinity
    
    short_distance[start] = 0

# The loop will keep running until we have entirely exhausted the graph, until we have seen all the nodes

# To iterate through the graph, we need to determine the min_distance_node every time.
    while remainingNodes: #Ensured that Actually seen all the nodes.
        min_distance_node = None

        for node in remainingNodes:

            if min_distance_node is None:
                min_distance_node = node

            elif short_distance[node] < short_distance[min_distance_node]:
                min_distance_node = node

# From the minimum node, what are our possible paths
    
        path_options = graph[min_distance_node].items()


# We have to calculate the cost each time for each path we take and only update it if it is lower than the existing cost

        for node_value, weight in path_options:
            
            if weight + short_distance[min_distance_node] < short_distance[node_value]:

                short_distance[node_value] = weight + short_distance[min_distance_node]

                track_predecessor[node_value] = min_distance_node

# We want to pop out the nodes that we have just visited so that we dont iterate over them again.
        remainingNodes.pop(min_distance_node)


# Once we have reached the destination node, we want trace back our path and calculate the total accumulated cost.

    currentNode = end

    while currentNode != start:

        try:
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    track_path.insert(0,start)

#  If the cost is infinity, the node had not been reached.
    if short_distance[end] != infinity:
        print('Shortest distance is ' + str(short_distance[end]))
        print('And the path is ' + str(track_path))


dijkstra(graph, '0', '8')
