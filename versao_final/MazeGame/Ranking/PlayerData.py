class PlayerData:
  # best_time: int (tempo em segundos ou milisegundos) PRECISA DEFINIR
  def __init__(self, name):
    self.__name = name
    self.__results = {} # [mode] -> best_time
       
    # self.__mode = mode
    # self.__best_time = best_time
    
  @property
  def name(self):
    return self.__name
  
  # @property
  # def mode(self):
  #   return mode
  
  # @property
  # def best_time(self):
  #   return best_time
  
  @property 
  def results(self):
    return self.__results

  def get_result(self, mode):
    if self.__results.get(mode):
      return self.__results.get(mode)
    else:
      return 0
  
  def update_points(self, mode, points):
    self.__results[mode] = points