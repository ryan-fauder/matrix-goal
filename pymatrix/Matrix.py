class Matrix:

  # Attributes
  nrows: int = 0
  ncols: int = 0
  data: list = []
  det: float = None
  
  def __init__(self, order: int):
    """
    Ceates a matrix by order
    :param order: order of the matrix
    """
    if order < 1:
        raise Exception('Invalid matrix size')
    self.data = [[0] * order] * order


  def __init__(self, matrix: list, nrows: int, ncolumns: int):
    """
    Creates a nrows by ncolumns matrix
    ### Parameters
      :param matrix: matrix
      :param nrows: number of rows
      :param ncolumns: number of columns
    """
    # matrix, nrows, ncolumns
    if nrows < 1 or ncolumns < 1:
        raise Exception('Invalid matrix size')
    self.data = [[0] * ncolumns] * nrows
    self.ncols = ncolumns
    self.nrows = nrows

  def __str__(self):
    if(self.data == [] or self.data == None):
      return "[]"
    table = "[\n"
    
    for vector in self.data:
      for item in vector:
        table += f"{item} "
      table += "\n"
    table += "]"

    return table

  def __repr__(self):
    if(self.data == [] or self.data == None):
      return "[]"
    table = "[\n"
    
    for vector in self.data:
      for item in vector:
        table += f"{item} "
      table += "\n"
    table += "]"

    return table

  
  def __add__(self, other):
    """
    Creates a nrows by ncolumns matrix
    ### Testes unitários
      - Soma entre matrizes inválidas
      - Soma entre matriz de tamanho
      - 
    """

    if not [self.nrows, self.ncols] == [other.nrows, other.ncols]:
      raise Exception('Not compatible matrixes')
    for i in range(0, self.nrows):
      for j in range(0, self.ncols):
        pass
  def __eq__(self, other):
    pass
  def __sub__(self, other):
    pass
  def __mul__(self, other):
   pass
  def __truediv__(self, other):
   pass
  def trace():
    pass
  def transpose():
    pass
  def cofactor(row: int, column: int):
    pass
  def cofactor_matrix():
    pass
  def adjugate():
    pass
  def inverse():
    pass