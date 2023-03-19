import geo

ip = geo.getIP()
print(ip)

country = geo.getCountry(ip, 'plain')
print(country)

country = geo.getCountry(ip, 'json')
print(country)

geoData = geo.getGeoData(ip)
print(geoData)

ptrData = geo.getPTR(ip)
print(ptrData)

geo.showIpDetails('2604:2dc0:100:271:0:0:0:0')

geo.showCountryDetails('2604:2dc0:100:271:0:0:0:0')
