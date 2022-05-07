from get_results import retrieveResults
from scores import scores
from get_results import get_baseset
from time import time
import networkx as nx
import pandas as pd

def main():
    """The Driver code for finding Hub & Authority Scores
    """
    query = ""
    # Main is the Input-ouput processing file 
    while query!="exit":
        print("Give your query to get results/press EXIT to end the loop : ")

        #Converting the input query into lower case
        query = input().lower()

        if query!="exit":
            print()
            start = time()
            root_set = retrieveResults(query)

            #Checking whether input query is present in any node
            if len(root_set) == 0:
                print("Your Query retrieved 0 results")
                return

            base_set, base_edges = get_baseset(root_set)

            #Sorting root set, base set, base edges
            root_set = sorted(root_set)
            base_set = sorted(base_set+root_set)
            base_edges = sorted(base_edges,key= lambda x:x[0])
            print("Root set :", root_set )
            print()
            print("Base set :", base_set)
            print()
            print("Edges :", base_edges)
            print()
            final_baseset = sorted(list(set(base_set+root_set)))
            
            if len(base_edges) > 0:
                h,a = scores(base_edges, final_baseset )
            else:
                h,a = {i:1 for i in final_baseset},{i:1 for i in final_baseset}
            end = time()
            temp = { "Node" : final_baseset, "Hub Score" : [h[i] for i in sorted(list(h.keys()))], "Authority Score" : [a[i] for i in sorted(list(a.keys()))]}
            df = pd.DataFrame(temp, index= None)
            df = df.set_index("Node")

            #Storing results into a excel sheet
            df.to_excel("results.xlsx")
            #df = df.remove

            #Finding the top 5 scores
            df1 = df.sort_values(by=['Hub Score'], ascending=False)
            print(df1["Hub Score"].head(min(5,len(df1))))
            print()
            df2 = df.sort_values(by=['Authority Score'], ascending=False)
            print(df2["Authority Score"].head(min(5,len(df2))))
            print()
            
            #print(df)
            print("Info retrieved in", end-start,"sec")

main()
