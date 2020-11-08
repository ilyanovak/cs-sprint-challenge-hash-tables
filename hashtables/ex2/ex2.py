#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    routes = {}

    for ticket in tickets:
        routes[ticket.source] = ticket.destination

    full_route = [""] * length
    full_route[0] = routes['NONE']

    for i in range(1, len(full_route)):
        full_route[i] = routes[full_route[i - 1]]

    return full_route
