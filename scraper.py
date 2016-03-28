import requests
import io
import html5lib
from bs4 import BeautifulSoup
import sys



DOMAIN_NAME = 'http://info.kingcounty.gov'
PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
PARAMS = {
    'Business_Name': 'Bamboo Garden',
    'Business_Address': '364 Roy st',
    'Longitude': '',
    'Latitude': '',
    'City': 'Seattle',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'B',
}


def get_inspection_page(**kwargs):
    # import pdb; pdb.set_trace()
    url = DOMAIN_NAME + PATH
    params = PARAMS.copy()
    for key, value in kwargs.items():
        if key in PARAMS:
            params[key] = value
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.content, response.encoding

# stuff = get_inspection_page()


def write_to_file(contents):
    f = io.open('inspection_page.html', 'w')
    f.write(contents)
    f.close()
    return f

# write_to_file(stuff)


def load_inspection(file):
    file = io.open(file, encoding='utf-8', mode='r')
    return file, 'utf-8'


def parse_source(file, encoding='utf-8'):
    parsed = BeautifulSoup(open(file), 'html5lib')

    return parsed


# def extract_meta_data(file):




def main():
    kwargs = {
        'Zip_Code': 98109,
        'Inspection_Start': '1/1/2016',
        'Inspection_End': '3/24/2016'
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        load_inspection('inspection_page.html')
    else:
        get_inspection_page(kwargs)

if __name__ == '__main__':
    main()











