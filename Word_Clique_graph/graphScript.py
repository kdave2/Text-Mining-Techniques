import networkx as nx



"""
Read the file structure and make a new Graph
"""

myGraph=nx.Graph()
f=open('input.txt')
for line in f:
    line=line.strip()
    toks=line.split(' ')
    myGraph.add_edge(toks[0],toks[1]) #this line adds the edge. It automaitcally adds the nodes of an edge, 
        #if the nodes have not already been added to the graph.

f.close()

print ('\nWE HAVE A GRAPH WITH ',myGraph.number_of_nodes(),'NODES AND ',myGraph.number_of_edges(),' EDGES.')
                                                                             
print ('THE GRAPH DIAMETER IS ',nx.diameter(myGraph))                                  

#print all the neighbors of node '32'
print ('NEIGHBORS OF NODE 32',myGraph.neighbors('32'))

#add information for a node
myGraph.node['32']['name']='Ted'
myGraph.node['32']['city']='Hoboken'
print ('INFO FOR NODE 32',myGraph.node['32'])

#add information for a connection (Edge) between 2 nodes
myGraph.edge['32']['25']['type']='friends'
myGraph.edge['32']['26']['type']='colleagues'
myGraph.edge['32']['26']['timestamp']=2011
print ('EDGE INFO FOR NODE 32', myGraph.edge['32'])



"""
#find all maximal cliques   
cliques=list(nx.find_cliques(myGraph))
sorted_cliques= sorted(cliques, key=len,reverse=True) # sort cliques by size
for cl in sorted_cliques:
    print cl
"""

