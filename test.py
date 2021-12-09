import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'pythonist.ru',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'pythonist.ru',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'pythonist.ru',
    'from': 'Alabama'
})

with open('data.txt', 'a') as outfile:
    json.dump(data, outfile)
    outfile.write("\n")
