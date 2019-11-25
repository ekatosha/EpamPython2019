import json
import re


# Parser for JSON string that consists of JSON array with JSON objects
def parse_json(lst):
    result = []
    structure = []
    stack = []
    pair = []
    for i, j in enumerate(lst):
        if '{' in j or '}' in j:
            for k in j:
                if k != '{' and k != '}':
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

        elif ':' in j and ':' in lst[i-1]:
            text = re.sub(r'\s+', ' ', j)
            pair.append(text)
            stack.append(pair)
            pair=[]
        elif ':' in j and ':' not in lst[i-1]:
            ex = j.strip()
            if len(ex)>1:
                pair.append(lst[i-1])
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
                            text = re.sub(r'\s+', ' ', text)
                            pair.append(text)
                        stack.append(pair)
                        pair = []
            else:
                pair.append(lst[i-1])
        elif ':' in lst[i-1] and ':' not in lst[i-2]:
            if pair:
                text = re.sub(r'\s+', ' ', j)
                pair.append(text)
                stack.append(pair)
                pair = []
    return result


# Delete duplicates in the list of dictionaries
def del_duplicate(lst):
    seen = set()
    final_d = []
    for d in lst:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            final_d.append(d)
    return final_d


# Dump for JSON array with Json objects. Works very slow with big list
def dump_json(lst):
    result = '['
    for _ in lst:
        items = tuple(_.items())
        s = ''
        for key, value in items:
            s += '"{}": "{}", '.format(key, value)
        result += '{' + s[:-2] + '}, '
    return result[:-2] + ']'


with open("C:/Users/ekant/Desktop/winedata_1.json") as f:
    s_1 = f.read()
    s_1 = s_1.replace('\\"', "'")
    # s_1 = s_1.encode().decode('unicode_escape')

with open("C:/Users/ekant/Desktop/winedata_2.json") as inf:
    s_2 = inf.read()
    s_2 = s_2.replace('\\"', "'")
    # s_2 = s_2.encode().decode('unicode_escape')


string = s_1+s_2
string = string.replace('null', 'None')
d = string.split('"')

result_parse = parse_json(d)
new_d = del_duplicate(result_parse)
print('Дубликатов:', len(result_parse)-len(new_d))

# Sort objects by price, then by wine sort

winedata = sorted(new_d, key=lambda x: '' if x['variety'] is None else x['variety'])
winedata = sorted(winedata, key=lambda x: -1 * float('inf') if x['price'] is None else x['price'], reverse=True)

result_json = dump_json(winedata)

f = open('winedata_full.json', 'tw', encoding='utf-8')
f.write(result_json)
f.close()
