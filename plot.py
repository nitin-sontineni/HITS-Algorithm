from get_results import retrieveResults
from scores import scores
from get_results import get_baseset
from time import time
from matplotlib import pyplot as plt
import pandas as pd
import random

def main():
    nodes_n = [i*(i-1)*0.25 for i in range(2,101)]
    time_n = []
    for i in range(2,101):
        """The Driver code for finding Hub & Authority Scores
        """

        base_set = [x for x in range(1,i)]
        edges = []
        counter = 0
        for x in range(1,i):
            for y in range(1,i):
                if x!=y and random.randint(1,100)%4 == 2:
                    edges.append((x,y))
                counter+=1
        if i%50 == 0 and i!=0:
            print(i)
        #print(len(edges))
        #base_edges = sorted(base_edges,key= lambda x:x[0])
        # print("Root set :", root_set )
        # print()
        # print("Base set :", base_set)
        # print()
        # print("Edges :", base_edges)
        # print()
        # final_baseset = sorted(list(set(base_set+root_set)))
        start = time()
        if len(edges) > 0:
            h,a = scores(edges, base_set,max_iter=500)
        # else:
        #     h,a = {i:1 for i in final_baseset},{i:1 for i in final_baseset}
        end = time()
        # temp = { "Node" : final_baseset, "Hub Score" : [h[i] for i in sorted(list(h.keys()))], "Authority Score" : [a[i] for i in sorted(list(a.keys()))]}
        # df = pd.DataFrame(temp, index= None)
        # df = df.set_index("Node")

        # #Storing results into a excel sheet
        # df.to_excel("results.xlsx")
        # #df = df.remove

        # #Finding the top 5 scores
        # df1 = df.sort_values(by=['Hub Score'], ascending=False)
        # print(df1["Hub Score"].head(min(5,len(df1))))
        # print()
        # df2 = df.sort_values(by=['Authority Score'], ascending=False)
        # print(df2["Authority Score"].head(min(5,len(df2))))
        # print()
        
        #print(df)
        time_n.append(end-start)
    plt.plot(nodes_n,time_n)
    plt.title("Run time Vs No Of Edges Plot")
    plt.xlabel("Number of Edges")
    plt.ylabel("Run time(in Secs)")
    plt.show()

main()