import json

j =''' { 
    "label":"Arun",
    "nav":[
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

result  = []
count = 0
def find_item(nav):
    na = nav.get('nav')
    label = nav.get('label')
    for element in na:
        print({'name':element.get('label'),'parent':label})
        if 'nav' in element:
            find_item(element)

with open('curry.json') as f:
    data = json.load(f)
    catalog = data.get('catalog')
    find_item(catalog)