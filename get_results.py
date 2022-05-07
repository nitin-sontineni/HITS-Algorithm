import networkx as nx
web_graph = nx.read_gpickle("web_graph.gpickle")
nodes = web_graph.nodes

def retrieveResults(query):
    """Retrieves required nodes for the given query

    Args:
        query (String): input query

    Returns:
        List : Nodes containing the input query
    """
    query = query.lower()
    results = []
    #Finding the nodes which contains the input query 
    for i in nodes:
        if query in nodes[i]['page_content'].lower():
            results.append(i)

    return results


def get_baseset(nodes):
    """Finds base set and base edges for the given root set

    Args:
        nodes (List): Root set

    Returns:
        List : Base set
        List : Base edges
    """
    edges = web_graph.edges
    base_set = set()
    base_edges = set()
    #Finding the edges containing the nodes in root set
    for node in nodes:
        for edge in edges:
                if node in edge:
                    base_edges.add(edge)
                if node == edge[0]:
                    base_set.add(edge[1])
                elif node == edge[1]:
                    base_set.add(edge[0])

    return list(base_set),list(base_edges)

