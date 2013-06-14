#!/bin/python
# encoding: utf-8
import networkx as nx
import matplotlib.pyplot as plt
class Add():
    def __init__(self,graph):
        self.graph = graph
        self.path = {}
        self.path_vertex = []

    def set_vertex_initial(self, vertexs):
        for position in self.graph.keys():
            for vertex, weight in self.graph.get(position).iteritems():
                if vertex in vertexs and position in vertexs and not((vertex,position)) in self.path:
                    self.path[(position,vertex)] = weight
        print "First Path: %s \n" %self.path

    def get_path_vertexs(self):
        for position in range(len(self.path.keys())):
            for vertex in self.path.keys()[position]:
                if not(vertex) in self.path_vertex:
                    self.path_vertex.append(vertex)
        self.path_vertex.sort()
                    
    def calculate_way(self):
        self.get_path_vertexs()        
        while self.path_vertex != self.graph.keys():
            menor_custo = 999999
            for vertex_graph in self.graph.keys():
                if not(vertex_graph in self.path_vertex):
                    for link_vertex in self.path.keys():
                        custo = 0
                        for vertex_path in link_vertex:
                            custo += self.graph.get(vertex_path).get(vertex_graph)
                        custo -= self.path.get(link_vertex)
                        if custo < menor_custo:
                            menor_custo = custo
                            link_vertex_menor_custo = link_vertex
                            vertex_menor_custo = vertex_graph
            print "Menor Custo: %s\nLigacao dos Vertices: %s %s" %(menor_custo, vertex_menor_custo, link_vertex_menor_custo)
            self.change_path(link_vertex_menor_custo, vertex_menor_custo)
    
    def change_path(self, link_vertex, vertex):
        self.path.pop(link_vertex)
        self.path[(vertex,link_vertex[0])] = self.graph.get(link_vertex[0]).get(vertex)
        self.path[(vertex,link_vertex[1])] = self.graph.get(link_vertex[1]).get(vertex)
        self.get_path_vertexs()
        print "Caminho: %s \n" %self.path
    
    def get_total_cost(self):
        total = 0
        for weight in self.path.values():
            total += weight
        return total

    def show_graph(self):
        graph=nx.Graph(self.graph)
        pos=nx.circular_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_color='r', node_size=500, alpha=0.8)
        nx.draw_networkx_edges(graph,pos,width=1,alpha=0.5)
        nx.draw_networkx_edges(graph,pos,
                        edge_labels={},
                        edgelist=self.path.keys(),
                        width=8,alpha=0.5,edge_color='r')
        nx.draw_networkx_edge_labels(graph,pos, self.get_list_weights_edge(),label_pos=0.3)
        labels=self.set_labels()
        nx.draw_networkx_labels(graph,pos,labels,font_size=16)
        plt.title("Caixeiro Viajante - ADD")
        plt.text(0.5, 0.97, "Path: "+str(self.path),
                            horizontalalignment='center',
                            transform=plt.gca().transAxes)
        plt.text(0.5, 0.90, "Custo Total: "+str(self.get_total_cost()),
                           horizontalalignment='center',
                           transform=plt.gca().transAxes)
        plt.axis('off')
        plt.show()
    
    def set_labels(self):
        labels={}
        for position in self.graph.keys():
            labels[position]=position
        return labels
    
    def get_list_weights_edge(self):
        list_weights_edge={}
        for position in self.graph.keys():
            for vertex, weight in self.graph.get(position).iteritems():
                if not(list_weights_edge.get((vertex,position))):
                    list_weights_edge[(position,vertex)] = weight
        return list_weights_edge

if __name__ == '__main__':
   print "Exemplo 1 - Graph"
   # graph = { 
   #            1: { 2: 3, 3: 4, 4: 3, 5: 6  },
   #            2: { 3: 1, 4: 7, 5: 4  },
   #            3: { 4: 2, 5: 5  },
   #            4: { 5: 5  },
   #            5: {  },
   #            }
   graph = {
        1: { 2: 3, 3: 4, 4: 3, 5: 6 },
        2: { 1: 3, 3: 1, 4: 7, 5: 4 },
        3: { 1: 4, 2: 1, 4: 2, 5: 5 },
        4: { 1: 3, 2: 7, 3: 2, 5: 5 },
        5: { 1: 6, 2: 4, 3: 5, 4: 5 },
   }
   add = Add(graph)
   add.set_vertex_initial([5,4,3])
   add.calculate_way()
   add.show_graph()