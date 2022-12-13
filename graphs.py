# Graph data structure 
class Graph:
  
      def __init__(self, nodes):
  
          self.nodes = nodes
  
          self.edges = {}
  
          self._build_edges()
  
      def _build_edges(self):
  
          for node in self.nodes:
  
              self.edges[node] = []
  
              for other_node in self.nodes:
  
                  if node != other_node:
  
                      self.edges[node].append(other_node)
  
      def get_edges(self):
  
          return self.edges
  
      def get_nodes(self):
  
          return self.nodes




