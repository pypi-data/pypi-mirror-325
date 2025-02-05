import TaloGameServicesApi as TaloApi

key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjE1NSwiYXBpIjp0cnVlLCJpYXQiOjE3Mzg3MTM4MTV9.tcAAX9Y5Mmtj-KJEbYkUj-HATdetEuKLsLHMWyMr-F4"

api = TaloApi.TaloGameServicesApi(key)


player = api.players.Identify("TaloPlayer", "Steam")

print(player)