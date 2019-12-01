import json
import re
import pandas as pd
import matplotlib.pyplot as plt


def parse_json(lst):
    result = []
    structure = []
    stack = []
    pair = []
    for i, j in enumerate(lst):
        if '{' in j or '}' in j:
            for k in j:
                if k !='{'and k != '}':
                    pass
                else:
                    if k == '{':
                        structure.append('{')
                    elif k == '}' and structure[-1] == '{':
                        structure.pop()
                        dict_temp = dict(stack)
                        result.append(dict_temp)
                        stack = []
                    else:
                        print('Error in structure')

        elif ':' in j and ':' in d[i-1]:
            pair.append(j)
            stack.append(pair)
            pair=[]
        elif ':' in j and ':' not in d[i-1]:
            ex = j.strip()
            if len(ex)>1:
                pair.append(d[i-1])
                l = ex.split()
                for k in l:
                    if k == ':':
                        pass
                    else:
                        text = re.sub('[^А-яA-z0-9]', '', k)
                        if text.isdigit():
                            pair.append(int(text))
                        elif text == 'None':
                            pair.append(None)
                        else:
                            pair.append(text)
                        stack.append(pair)
                        pair = []
            else:
                pair.append(d[i-1])
        elif ':' in d[i-1] and ':' not in d[i-2]:
            if pair != []:
                if j.isdigit():
                    pair.append(int(j))
                else:
                    pair.append(j)
                stack.append(pair)
                pair=[]
    return result


def del_duplicate(lst):
    seen = set()
    final_d = []
    for d in lst:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            final_d.append(d)
    return final_d


def dump_json_object(d):
    s = ''
    for key, value in d.items():
        if value == str(value):
            s += '"{}": "{}", '.format(key, value)
        elif type(value) == list:
            l = '['
            for i in value:
                l += '"{}", '.format(i)
            l = l[:-2] + ']'
            s += '"{}": {}, '.format(key, l)
        else:
            s += '"{}": {}, '.format(key, value)
    return '{'+s[:-2]+'}'


with open("C:/Users/ekant/Desktop/winedata_1.json") as f:
    s_1 = f.read()
    s_1 = s_1.replace('\\"', "'")
    s_1 = s_1.encode().decode('unicode_escape')

with open("C:/Users/ekant/Desktop/winedata_2.json") as inf:
    s_2 = inf.read()
    s_2 = s_2.replace('\\"', "'")
    s_2 = s_2.encode().decode('unicode_escape')


string = s_1+s_2
string = string.replace('null', 'None')
string = string.replace('Gewürztraminer', 'Gewurztraminer')
string = string.replace("\'", "'")
d = string.split('"')

result_parse = parse_json(d)
new_d = del_duplicate(result_parse)

for i in new_d:
    if 'Madera' in i['title']:
        i['Madera'] = 'Madera'
    else:
        i['Madera'] = None

winedata = sorted(new_d, key=lambda x: '' if x['variety'] is None else x['variety'])
winedata = sorted(winedata, key=lambda x: -1 * float('inf') if x['price'] is None else x['price'], reverse = True)

df = pd.DataFrame(winedata)

wine_sort = ['Gewurztraminer', 'Riesling', 'Madera', 'Merlot', 'Tempranillo', 'Red Blend']
wine = {}
for i in wine_sort:
    if i == 'Madera':
        temp = 'Madera'
    else:
        temp = 'variety'
    d_temp = {}
    d_temp['avarege_price'] = df[df[temp] == i]['price'].mean()
    d_temp['min_price'] = min(df[df[temp] == i]['price'])
    d_temp['max_price'] = max(df[df[temp] == i]['price'])
    df_country = df[df[temp] == i].groupby(['country']).count()
    df_country = df_country.reset_index()
    d_temp['most_common_country'] = df_country['country'].where(df_country['points'] == max(df_country['points'])).dropna().item()
    df_r = df[df[temp] == i].groupby(['region_1']).count()
    df_r = df_r.reset_index()
    d_temp['most_common_region'] = df_r['region_1'].where(df_r['points'] == max(df_r['points'])).dropna().item()
    d_temp['average_score'] = df[df[temp] == i]['points'].mean()
    wine[i] = dump_json_object(d_temp)
    d_temp = {}
print('Статистика для заданных сортов вин', wine)

wines = {}
wines['wine'] = dump_json_object(wine)

statistics = {}

most_expensive_wine = df['title'].where(df['price'] == max(df['price'])).dropna()
statistics['most_expensive_wine'] = most_expensive_wine.item()

cheapest_wine = df['title'].where(df['price'] == min(df['price'])).dropna()
statistics['cheapest_wine'] = list(cheapest_wine.to_numpy())

highest_score = df['title'].where(df['points'] == max(df['points'])).dropna()
statistics['highest_score'] = list(highest_score.to_numpy())

lowest_score = df['title'].where(df['points'] == min(df['points'])).dropna()
statistics['lowest_score'] = list(lowest_score.to_numpy())

df1 = df[['country', 'price']]
df1 = df1.groupby(['country']).mean()
df1 = df1.reset_index()
#print(df1.sort_values(by=['price'], ascending=False))

most_expensive_country = df1['country'].where(df1['price'] == max(df1['price'])).dropna()
statistics['most_expensive_country'] = most_expensive_country.item()

cheapest_coutry = df1['country'].where(df1['price'] == min(df1['price'])).dropna()
statistics['cheapest_coutry'] = cheapest_coutry.item()

df2 = df[['country', 'points']]
df2 = df2.groupby(['country']).mean()
df2 = df2.reset_index()

most_rated_country = df2['country'].where(df2['points'] == max(df2['points'])).dropna()
statistics['most_rated_country'] = most_rated_country.item()

underrated_country = df2['country'].where(df2['points'] == min(df2['points'])).dropna()
statistics['underrated_country'] = underrated_country.item()

df4 = df[['taster_twitter_handle']]
df4['count'] = df4['taster_twitter_handle'].copy()
df4 = df4.groupby(['taster_twitter_handle']).count()
df4 = df4.reset_index()
#print(df4.sort_values(by=['count'], ascending  = False))
most_active_commentator = df4['taster_twitter_handle'].where(df4['count'] == max(df4['count'])).dropna()
statistics['most_active_commentator'] = most_active_commentator.item()

wines.update(statistics)

final_statistics = {}
final_statistics['statistics'] = dump_json_object(wines)

result = dump_json_object(final_statistics)
result = result.replace('"{', '{')
result = result.replace('}"', '}')

f = open('stats.json', 'tw', encoding='utf-8')
f.write(result)
f.close()
