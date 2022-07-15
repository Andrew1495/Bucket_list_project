from models.country import Country
from models.city import City
from models.user import User

import repositories.user_repo as user_repo

import repositories.country_repo as country_repo
import repositories.city_repo as city_repo

country1 = Country("Scotland", "Europe")

country_repo.save(country1)

city1 = City("Edinburgh", country1)
city_repo.save(city1)

user1 = User("andrew")
user_repo.save(user1)

