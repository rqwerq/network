
import argparse
from network import Network
from demand import ODMatrix,Connector,update_odMatrix
import util
from assignment import all_or_nothing_assignment

from visualize import draw_network

def main():
    
    parser = argparse.ArgumentParser(description="UESTC Transport Assignment system")
   
    parser.add_argument("-n", help="network file")
   
    parser.add_argument("-d", help="demand file")
    parser.add_argument("-e", help="elements in diagram")
    parser.add_argument("-o", help="output diagram file")
  

   
    roadMap =Network()
    
    roadMap.make_example()
  
  
    connector =Connector(roadMap.nodes())
    result =connector.get_ods_and_indices()
    
    odMatrix =ODMatrix(n=len(connector.nodeids))
   
    update_odMatrix(odMatrix,connector,('a','e'),10)
    update_odMatrix(odMatrix,connector,('a','d'),2)
    update_odMatrix(odMatrix,connector,('b','d'),1)
    update_odMatrix(odMatrix,connector,('c','e'),5)
    update_odMatrix(odMatrix,connector,('d','e'),3)
    update_odMatrix(odMatrix,connector,('e','c'),9)
    
    flowBundle =all_or_nothing_assignment(roadMap,odMatrix,connector)
   
    flowMap =util.FlowMap(roadMap)
    util.bundle_to_map(flowMap,flowBundle)
    
    flowMap_flows_keys =list(flowMap.flows.keys())
    for route in flowMap_flows_keys:
        if route in flowMap.flows.keys():
            if flowMap.flows[route] ==0:
                flowMap.flows.pop(route)
                continue
            if (route[1],route[0]) in flowMap.flows.keys() and route in flowMap.flows.keys():
              
                flowMap.flows[route] +=flowMap.flows[(route[1],route[0])]
                flowMap.flows.pop((route[1],route[0]))

    draw_network(roadMap,flowBundle)
if __name__ == "__main__":
    main()