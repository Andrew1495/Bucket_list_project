from models.country import Country
import repositories.countries_repo as countries_repo

country1 = Country("Scotland", "Europe")

countries_repo.save(country1)