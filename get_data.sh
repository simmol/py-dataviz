# Make dir if does not exist
mkdir -p data

# Download data files in data dir. Override files
wget -O ./data/airports.dat https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat

wget -O ./data/airlines.dat https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat

wget -O ./data/routes.dat https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat
