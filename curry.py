import json
import pprint as pp
import typing
import jsontree  


j =''' { "nav":[
                      {
                         "label":"Washing machines",
                         "link":"https://www.currys.co.uk/gbuk/household-appliances/laundry/washing-machines/332_3119_30206_xx_xx/xx-criteria.html",
                         "nav":[
                            {
                               "label":"All",
                               "link":"https://www.currys.co.uk/gbuk/household-appliances/laundry/washing-machines/332_3119_30206_xx_xx/xx-criteria.html"
                            },
                            {
                               "label":"Freestanding",
                               "link":"https://www.currys.co.uk/gbuk/freestanding-washing-machines/laundry/washing-machines/332_3119_30206_xx_ba00010669-bv00308556/xx_xx_xx_xx_5-6-7-8-9-10-11-criteria.html"
                            },
                            {
                               "label":"Integrated",
                               "link":"https://www.currys.co.uk/gbuk/integrated-washing-machines/laundry/washing-machines/332_3119_30206_xx_ba00010669-bv00308557/xx-criteria.html"
                            }
                                ]
                        }
                    ]
        }'''

result = []

def item_generator(nav,parent):
    for element in nav:
        result.append( {'category_name' : element.get('label'),
                        'parent_category':parent})
        if 'nav' in element:
            parent = element.get('label')
            item_generator(element.get('nav'),parent)

def item_generator2(nav,parent):
    for i in range(len(nav)):
        label = nav[i].get('nav')
        result.append( {'category_name' : label,
                        'parent_category':parent})
        if 'nav' in nav[i]:
            item_generator2(nav[i],label)


def find(nav_obj):
    nav = nav_obj.get('nav')
    label = nav_obj.get('label')
    for element in nav:
        print(label)
        if 'nav' in element:
            return find(element)

with open('curry.json') as f:
    data = json.load(f)
    catalog = data.get('catalog')
    # print(type(catalog))
    # nav = catalog.get('nav')
    print(find(catalog))

    # item_generator(nav,None)
    #from flatten_json import flatten
    #pp.pprint(flatten(catalog,root_keys_to_ignore='link'))
print(pp.pprint(result))
with open('nav.json','w') as fi:
    json.dump(result,fi)