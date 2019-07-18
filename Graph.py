class Vertex(object):
  """docstring for Vertex"""
  edges = []
  def __init__(self,number,edge=None):
    super(Vertex, self).__init__()
    self.number = number
    self.edges.append(edge) if edge else 0

  def add_edge(self, edge):
    self.edges.append(edge)

  def __str__(self):
    output = "Number: " + str(self.number)
    for edge in self.edges:
      print(edges)
    return output

class Edge(object):
  """docstring for Edge"""
  def __init__(self, source, dest):
    super(Edge, self).__init__()
    self.source = source
    self.dest = dest

  def __str__(self):
    return "Source :" + str(self.source) + "Dest: "+ str(self.dest)

class Graph(object):
  """docstring for Graph"""
  edges = [None] * 5
  vertices = [None] * 5

  def __init__(self):
    super(Graph, self).__init__()

  def add_vertex(self,number, source=None):
    vertex = Vertex(number)
    self.vertices[number] = vertex
  
  def add_edge(source, dest):
    source = vertices[source]
    dest = vertices[dest]
    edge = Edge(source, dest)

    source.add_edge(edge)
    dest.add_edge(edge)

    self.edges.append(edge)

  def graph(self):
    return self.edges, self.vertices
    
    