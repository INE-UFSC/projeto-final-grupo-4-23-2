import pickle
import sys
from MazeGame.Ranking.PlayerData import PlayerData

class DAO:
    def __init__(self, datasource='ranking_data'):
      self.datasource = datasource
      self.cache = {}  # Um dicionário que atua como um cache de objetos

      try:
        self.cache = pickle.load(open(self.datasource, 'rb')) # Tentativa de carregar os dados do arquivo

      except FileNotFoundError:
          self.dump()  # Se o arquivo não existe, cria um arquivo vazio

    def dump(self):
      arquivo = open(self.datasource, 'wb')
      pickle.dump(self.cache, arquivo)
      arquivo.close()

    def add(self, name, mode, points):
      player_data = self.cache.get(name)
      
      if not player_data:
        player_data = PlayerData(name)
        player_data.update_points(mode, points)
        
      self.cache[name] = player_data
      self.dump()  # Salva o cache atualizado no arquivo
    
    def get_all_players_data(self):
      return self.cache
     
    def get_player_data(self, name):
      return self.cache.get(name)
    
    def update_player_data(self, name, mode, points):
      try:
        self.cache[name].update_points(mode, points)
        self.dump()
      except KeyError:
        raise

    def remove(self, key, obj):
      try:
        self.cache.pop(key)  # Remove um objeto pelo sua chave
        self.dump()  # Salva o cache atualizado no arquivo
        return True
      except KeyError:
        raise  # Se a chave não existe no cache, levanta uma exceção
