import math
import networkx as nx
# Loading data to test
#print(list(web_graph.edges))

# defining error to see if the system reached near-steady state

def error(l1,l2):
    """error : Quantifies the differences in 2 dictionaries with same keys

    Args:
        l1 (Dictionary): A Non-empty dictionary
        l2 (Dictionary): A Non-empty dictionary

    Returns:
        Float : Average of differences of values of respective common keys in two dictionaries 
    """    
    return sum(abs(l1[n] - l2[n]) for n in l1)/len(l1)

def scores(edges,n,max_iter=100,tol=10**-8): # n = list of nodes
    """scores : Hub and Authoritative scores of Nodes

    Args:
        edges (List[Tuples(Node,Node)]): A (NodeA,NodeB) tuple suggests a directed edge from NodeA to NodeB
        n (List[Nodes]): The IDs of Nodes
        max_iter (int, optional): The Maximum Iterations allowed for the system to converge. Defaults to 100.
        tol (_type_, optional): The error value at which the system is considered convereged. Defaults to 10**-8.

    Returns:
        Dictionary, Dictionary: Hubs and Authority scores as dictionaries with (key,value) = (Node, score)
    """    
    # initialising h,a with 1s
    h,a = {i:1/len(n) for i in n},{i:1/len(n) for i in n}

    i,flag = 0,0
    for count in range(max_iter):
        # initialising a new h,a score dictionary for finding new scores in this iteration
        h1,a1 = {i:0 for i in n},{i:0 for i in n}

        #summing corresponding node scores
        while i<len(edges):
            h1[edges[i][0]]+=a[edges[i][1]]
            a1[edges[i][1]]+=h[edges[i][0]]
            i+=1

        # finding the norm for normalising the scores - h1
        norm = 0
        for x in h1:
            norm+=h1[x]#**2
        # norm = math.sqrt(norm)
        for x in h1:
            h1[x] /= norm

        # finding the norm for normalising the scores - a1
        norm = 0
        for x in a1:
            norm+=a1[x]#**2
        # norm = math.sqrt(norm)
        for x in a1:
            a1[x] /= norm

        # Check if system reached a near staedy state
        if error(h,h1)<tol and error(a,a1)<tol:
            # print(error(h,h1))
            # print(error(a,a1))
            print("Converged @",str(count) + "th","Iteration")
            flag = 1
            break

        else:
            i = 0

        h, a = h1, a1

    if flag == 0:
        print("Reached Max-iteration limit")
    return h, a

# def graph_creater(edges,nodes):
#     G = nx.DiGraph()
#     G.add_nodes_from(nodes)
#     G.add_edges_from(edges)
#     return G

#testing the algo. correctness     
if __name__ == "__main__":  
    web_graph = nx.read_gpickle("web_graph.gpickle")
    scores(list(web_graph.edges),list(web_graph.nodes))



        
