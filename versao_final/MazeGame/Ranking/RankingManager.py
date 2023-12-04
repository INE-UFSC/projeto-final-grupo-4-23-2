from MazeGame.Ranking.DAO import DAO

class Singleton(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
    return cls._instances[cls]

class RankingManager(metaclass=Singleton):
  _instance = None 
  
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
        # Inicialização de instância aqui, se necessário.
    return cls._instance
    
  def __init__(self):
    self.__dao = DAO()
    print(self.__dao.cache)
  
  def get_results_by_mode(self, mode):
    results = self.__dao.get_all_players_data()
    
    results_mode = {}
    
    for r in results:
      time = r.get_result(mode)
      if time:
        results_mode[r.name] = time ## Seria ideal criar uma DTO para esse tipo de informação
        
    return results_mode
  
  def get_results_by_player(self, name):
    player_data = self.__dao.get_player_data(name)
    
    if player_data:
      return player_data.results
    
  def set_player_new_result(self, name, mode, points):
    player_data = self.__dao.get_player_data(name)
    
    if player_data and player_data.get_result(mode) < points:
      player_data.update_points(mode, points)
      self.__dao.dump()
    elif not player_data:
      self.__dao.add(mode=mode, name=name, points=points)