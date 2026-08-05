class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stb = defaultdict(list)
        for bus_id,stops in enumerate(routes):
            for stop in stops:
                stb[stop].append(bus_id)

        queue = deque([(source,0)])

        visited_stops = {source}
        visited_bus = set()

        while queue:
            current_stop,buses_taken = queue.popleft()

            for b in stb[current_stop]:
                if b not in visited_bus:
                    visited_bus.add(b)
                    for next_stop in routes[b]:
                        if next_stop == target:
                            return buses_taken + 1
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop,buses_taken + 1))


        return -1

