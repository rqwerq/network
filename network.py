from heapq import heappush, heappop

class Network:
    def __init__(self):
        self._neighbours = {}
        self._attributes = {}

    def make_example(self):
        self._neighbours = {
            'a':['b','d'],
            'b':['a','c','d'],
            'c':['b','d','e'],
            'd':['a','b','c','e'],
            'e':['c','d']
         }

        self._attributes = {
            "distance": {
                ('a','b'):4,
                ('a','d'):2,
                ('b','c'):4,
                ('b','d'):1,
                ('c','d'):1,
                ('c','e'):3,
                ('d','e'):7
            },
        }
    # 1. 增删查改
    def add_node(self, nodeid):
        assert nodeid not in self._neighbours

        self._neighbours[nodeid] = []

    def remove_node(self, nodeid):
        None

    def add_link(self, from_nodeid, to_nodeid):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        assert to_nodeid not in self._neighbours[from_nodeid]

        self._neighbours[from_nodeid].append(to_nodeid)

    def remove_link(self, from_nodeid, to_nodeid):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        assert to_nodeid in self._neighbours[from_nodeid]
        
        self._neighbours[from_nodeid].remove(to_nodeid)
        for attribute in self._attributes.values():
            del attribute[(from_nodeid, to_nodeid)]

    # 2. 查询
    def next_nodes(self, nodeid):
        return self._neighbours[nodeid]

    def prev_nodes(self, nodeid):
        None

    def is_connected(self, from_nodeid, to_nodeid):
        None

    def nodes(self):
        return self._neighbours.keys()

    def links(self):
        links = []

        for cur_node, next_nodes in self._neighbours.items():
            for next_node in next_nodes:
                links.append((cur_node, next_node))

        return links

    # 3. 属性
    def attributes(self, from_nodeid, to_nodeid):
        None

    def cost(self, road):
        from_nodeid,to_nodeid =road
        if (from_nodeid,to_nodeid) in self._attributes['distance']:
            return self._attributes['distance'][(from_nodeid,to_nodeid)]
        else:
            return self._attributes['distance'][(to_nodeid,from_nodeid)]

    def shortest_route(self, od):
        origin, destination = od
        ik_road = self.shortest_routes_from(origin)

        for route in ik_road.keys():
            if route[-1] == destination:
                return route
                
    # 4. 最短路径搜索
    def init_uk_road(self,keynode,uk_road,uk_node):
         for node in self._neighbours.keys():
             if (node==keynode):
                 for i in range(len(self._neighbours[keynode])):
                     road =(keynode,self._neighbours[keynode][i])
                     uk_road[road] =self.cost(road)
             else:
                 uk_node.append(node)
                 road =(keynode,node)
                 if road not in uk_road.keys():
                     uk_road[road] =float('inf')
         return uk_road
        
        
    def add_ik_road(self,ik_road,uk_road,ik_node,uk_node):
        minRoad =min(uk_road.values())
        for road in uk_road.keys():
            if (minRoad ==uk_road[road]):
                ik_road[road]=minRoad
                ik_node.append(road[len(road)-1])
                uk_node.remove(road[len(road)-1])
                return

    def find_road(self,end,roadList):
        for road in roadList.keys():
            if road[len(road)-1]==end:
                return road 


    def update_uk_road(self,uk_road,ik_road,ik_node,uk_node):
        newNode =ik_node[len(ik_node)-1]
        delUkRoad =self.find_road(newNode,uk_road)
        uk_road.pop(delUkRoad)
        for road in self.links():
            if newNode in road
                otherNode = road[0] if road[1]==newNode else road[1]    
                if otherNode in uk_node:
                    IkRoad =self.find_road(newNode,ik_road)
                    temp =ik_road[IkRoad]+self.cost(road)
                    ukRoad =self.find_road(otherNode,uk_road)
                    if (temp<=uk_road[ukRoad]):
                        newUkRoad =IkRoad+(otherNode,)    
                        uk_road.pop(ukRoad)             
                        uk_road[newUkRoad] =temp
                    
                    

    def shortest_routes_from(self,keynode):
        ik_node =[]
        uk_node =[]
        ik_road ={}
        uk_road ={}
        self.init_uk_road(keynode,uk_road,uk_node)
        while (uk_road):
            self.add_ik_road(ik_road,uk_road,ik_node,uk_node)
            self.update_uk_road(uk_road,ik_road,ik_node,uk_node)
        return ik_road

if __name__ =='__main__':
    roadmap =Network()
    roadmap.make_example()
    ik_road =roadmap.shortest_routes_from("a")
    print(ik_road)
