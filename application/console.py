
from models.country import Country
from models.city import City
from models.user import User
import repositories.user_repo as user_repo
import repositories.country_repo as country_repo
import repositories.city_repo as city_repo
import repositories.visit_repo as visit_repo
import repositories.want_to_visit_repo as want_to_visit_repo


want_to_visit_repo.delete_all()
visit_repo.delete_all()
user_repo.delete_all()
city_repo.delete_all()
country_repo.delete_all()

country_1 = Country("Scotland", "Europe")
country_2 = Country("England", "Europe")
country_3 = Country("Spain", "Europe")
country_4 = Country("China", "Asia")
country_5 = Country("Japan", "Asia")
country_6 = Country("U.S.A", "North America")
country_7 = Country("Brazil", "South America")
country_8 = Country("New Zealand", "Oceania")
country_9 = Country("Nigeria", "Africa")
country_10 = Country("Chile", "South America")
country_11 = Country("Italy", "Europe")
country_12 = Country("France", "Europe")
country_13 = Country("Canada", "North America")

country_repo.save(country_1)
country_repo.save(country_2)
country_repo.save(country_3)
country_repo.save(country_4)
country_repo.save(country_5)
country_repo.save(country_6)
country_repo.save(country_7)
country_repo.save(country_8)
country_repo.save(country_9)
country_repo.save(country_10)
country_repo.save(country_11)
country_repo.save(country_12)
country_repo.save(country_13)



city_1 = City("Edinburgh", country_1,"Arthur's Seat","Edinburgh Castle","Royal Yacht Britannia")
city_2 = City("London", country_2,"Tower Bridge" ,"Big Ben" ,"Tower of London" )
city_3 = City("Madrid", country_3, "Prado National Museum" , "Parque del Retiro" ,"Santiago Bernabeu Stadium")
city_4 = City("Glasgow", country_1, "Glengoyne Distillery" ,"Glasgow Science Centre" , "The Clydeside Distillery")
city_5 = City("Liverpool", country_2, "Anfield Stadium" , "Royal Albert Docks", "The Beatles Story")
city_6 = City("Manchester", country_2, "National Football Museum" , "Old Trafford" , "Etihad Stadium")
city_7 = City("New York City", country_6, "Empire State Building" , "Statue of Liberty", "Central Park")
city_8 = City("Austin", country_6, "Texas State Capitol" , "Barton Springs Pool", "Mount Bonnell")
city_9 = City("Beijing", country_4, "Forbidden City" , "Summer Palace", "Temple of Heaven")
city_10 = City("Shanghai", country_4, "The Bund" , "Shanghai Tower", "Yu Garden")
city_11 = City("Tokyo", country_5, "Meiji Jingu Shrine" , "Shinjuku Gyoen National Garden", "Yomiuri Land")
city_12 = City("Kyoto", country_5, "Fushimi Inari-taisha Shrine" , "Kinkakuji Temple", "Sanjusangendo Temple")
city_13 = City("Auckland", country_8, "SkyTower" , "Auckland Botanic Gardens", "Karekare Beach")
city_14 = City("Queenstown", country_8, "Queenstown Hill" , "Lake Wakatipu", "Kiwi Park")
city_15 = City("Lagos", country_9, "Lekki Conservation Centre" , "Tarkwa Bay Beach", "Freedom Park Lagos")
city_16 = City("Abuja", country_9, "Jabi Boat Club" , "Abuja National Mosque", "Jabi Lake")
city_17 = City("Rio de Janeiro", country_7, "Sugarloaf Mountain" , "Corcovado - Christ the Redeemer", "Botanical Garden")
city_18 = City("São Paulo", country_7, "Parque Ibirapuera" , "Paulista Avenue", "Neo Quimica Arena")
city_19 = City("Paris", country_12, "Eiffel Tower" , "Sainte-Chapelle", "Cathédrale Notre-Dame de Paris")
city_20 = City("Nantes", country_12, "Jardin des Plantes" , "Les Machines de L'ile", "Passage Pommeraye")
city_21 = City("Venice", country_11, "Doge's Palace" , "Basilica di San Marco", "Canal Grande")
city_22 = City("Rome", country_11, "Colosseum" , "Pantheon", "Roman Forum")
city_23 = City("Quebec City", country_13, "Old Quebec" , "Parc de la Chute-Montmorency", "Terrasse Dufferin")
city_24 = City("Toronto", country_13, "St. Lawrence Market" , "Royal Ontario Museum", "Hockey Hall of Fame")
city_25 = City("Santiago", country_10, "Cerro San Cristobal" , "Sky Costanera", "Cerro Santa Lucia")
city_26 = City("Valparaíso", country_10, "La Sebastiana" , "Cerro Concepción", "Paseo Gervasoni")



city_repo.save(city_1)
city_repo.save(city_2)
city_repo.save(city_3)
city_repo.save(city_4)
city_repo.save(city_5)
city_repo.save(city_6)
city_repo.save(city_7)
city_repo.save(city_8)
city_repo.save(city_9)
city_repo.save(city_10)
city_repo.save(city_11)
city_repo.save(city_12)
city_repo.save(city_13)
city_repo.save(city_14)
city_repo.save(city_15)
city_repo.save(city_16)
city_repo.save(city_17)
city_repo.save(city_18)
city_repo.save(city_19)
city_repo.save(city_20)
city_repo.save(city_21)
city_repo.save(city_22)
city_repo.save(city_23)
city_repo.save(city_24)
city_repo.save(city_25)
city_repo.save(city_26)



user = User("Andrew" , False)
user_repo.save(user)


