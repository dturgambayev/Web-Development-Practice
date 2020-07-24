import webbrowser

# Comparing counties' names and their links in Wikipedia
wiki_countries = {
    'Russia': 'Russia',
    'Canada': 'Canada',
    'United States': 'United_States',
    'China': 'China',
    'Brazil': 'Brazil',
    'Australia': 'Australia',
    'India': 'India',
    'Argentina': 'Argentina',
    'Kazakhstan': 'Kazakhstan',
    'Algeria': 'Algeria',
    'DR Congo': 'Democratic_Republic_of_the_Congo',
    'Greenland': 'Greenland',
    'Saudi Arabia': 'Saudi_Arabia',
    'Mexico': 'Mexico',
    'Indonesia': 'Indonesia',
    'Sudan': 'Sudan',
    'Libya': 'Libya',
    'Iran': 'Iran',
    'Mongolia': 'Mongolia',
    'Peru': 'Peru',
    'Chad': 'Chad',
    'Niger': 'Niger',
    'Angola': 'Angola',
    'Mali': 'Mali',
    'South Africa': 'South_Africa',
}

Asia = ['Asia', 'Russia', 'China', 'India', 'Kazakhstan', 'Mongolia', 'Saudi Arabia', 'Iran']
Africa = ['Africa', 'Algeria', 'DR Congo', 'Sudan', 'Libya', 'Chad', 'Niger', 'Mali', 'South Africa', 'Angola', 'Algeria']
North_America = ['North_America', 'Canada', 'United States', 'Greenland']
South_America = ['South_America', 'Brazil', 'Argentina', 'Mexico', 'Peru']
Oceania = ['Oceania', 'Australia', 'Greenland', 'Indonesia']
Continents = [Asia, Africa, North_America, South_America, Oceania]

flag = True
while flag:
    country_name = input('Please, type the name of the country: ')
    if country_name in wiki_countries:
        for i in Continents:
            if country_name in i:
                print('Here is a continent where ' + country_name + ' is located: ' + i[0])
                webbrowser.open('https://ru.wikipedia.org/wiki/' + wiki_countries[country_name])
                print('Here is a wikipedia link: ' + 'https://ru.wikipedia.org/wiki/' + wiki_countries[country_name])
                flag = False
    else:
        print('Invalid country, please try again!')
