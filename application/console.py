from curses.ascii import US
from models.country import Country
from models.city import City
from models.user import User
from models.visit import Vist
from models.want_to_visit import WantToVisit

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
country_repo.save(country_1)
country_repo.save(country_2)
country_repo.save(country_3)



city_1 = City("Edinburgh", country_1)
city_2 = City("London", country_2)
city_3 = City("Madrid", country_3)
city_4 = City("Glasgow", country_1)
city_5 = City("Liverpool", country_2)
city_6 = City("Manchester", country_2)
city_7 = City("Barcelona", country_3)
city_8 = City("Sevilla", country_3)
city_repo.save(city_1)
city_repo.save(city_2)
city_repo.save(city_3)
city_repo.save(city_4)
city_repo.save(city_5)
city_repo.save(city_6)
city_repo.save(city_7)
city_repo.save(city_8)


user_1 = User("Andrew")
user_repo.save(user_1)

visited_1 = Vist(user_1, city_1)
want_to_visit_1 = WantToVisit(user_1, city_2)

visit_repo.save(visited_1)
want_to_visit_repo.save(want_to_visit_1)

bucket = want_to_visit_repo.select(1)

print(bucket.__dict__)



