from curses.ascii import US
from models.country import Country
from models.city import City

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
country_repo.save(country_1)
country_repo.save(country_2)
country_repo.save(country_3)
country_repo.save(country_4)
country_repo.save(country_5)
country_repo.save(country_6)
country_repo.save(country_7)
country_repo.save(country_8)
country_repo.save(country_9)



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




