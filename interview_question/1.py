# find the minimum cost of travelling between two tram station in a circcular city with N station numbered from 1 to N, the cost of tickets between adjacent stations is given in an array ticket_cost , where ticket_cost[i] represents the cost of travelling from station i to i+1 % N. Trams can move in both clockwise and anticlockwise directions, the input includes N, the start station and the  finish station , the output shoud be minimum cost of travelling from start to finish station

def sum_clockwise(ticket_cost, start, finish, N):
    sum_cw = 0
    current = start
    while current != finish:
        sum_cw += ticket_cost[current]
        current = (current + 1) % N
    return sum_cw

def sum_anticlockwise(ticket_cost, start, finish, N):
    sum_acw = 0
    current = start
    while current != finish:
        current = (current - 1 + N) % N
        sum_acw += ticket_cost[current]
    return sum_acw

def minimum_travel_cost(N, ticket_cost, start, finish):
    # Convert to zero-based indices
    start -= 1
    finish -= 1
    
    # If start and finish are the same, no cost is needed
    if start == finish:
        return 0
    
    # Calculate the costs
    clockwise_cost = sum_clockwise(ticket_cost, start, finish, N)
    anticlockwise_cost = sum_anticlockwise(ticket_cost, start, finish, N)
    print('cl', clockwise_cost)
    print("anti", anticlockwise_cost)
    # Return the minimum of the two costs
    return min(clockwise_cost, anticlockwise_cost)



# Example usage:
N = 5
ticket_cost = [1, 2, 4, 4, 5]
start = 1
finish = 5
print(minimum_travel_cost(N, ticket_cost, start, finish))  # Output should be the minimum cost