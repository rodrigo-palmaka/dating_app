
import json
import requests

class find_restaurant:


    api_token = 'dafac7887518c8891eac8cb9c4c15453'
    # api_url_base = 'https://developers.zomato.com/api'
    base = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json','user-key' : api_token}

    # self.city_ID = None
    # self.cuisine_ID = None
    #
    # self.res_dict = {}

    def get_city_ID(self, CITY_NAME):
        # global city_ID
        self.cityName = CITY_NAME
        prms = {'q' : CITY_NAME}

        if type(CITY_NAME) is not str:
            raise Exception('Invalid Name Format')

        try:
            r = requests.get(url = self.base + "cities", headers = self.headers, params = prms)
            if r.status_code == 200:
                # print(r.text)
                data = r.json()
                if 'name' in data['location_suggestions'][0]:
                    # print(data['location_suggestions'][0]['id'])
                    self.city_ID = data['location_suggestions'][0]['id']
                    return True
                else:
                    raise Exception('No City Found')
            else:
                print('Error: 400')
        except IndexError:
            return False


    def get_cuisine(self, cuisine):
        # global cuisine_ID
        try:
            r = requests.get(url = self.base + "cuisines", headers = self.headers, params = {"city_id" : self.city_ID})
            data = r.json()
            # print(data)
            cus_index = data['cuisines']
            for i in cus_index:
                if i['cuisine']['cuisine_name'].lower() == cuisine.lower():
                    self.cuisine_ID = i['cuisine']['cuisine_id']
                    return self.cuisine_ID
            # print(data)
                # cuisine_ID =
        except IndexError:
            print("Invalid Cuisine")


    def get_rest_list(self, city, cuis):
        # global rest_dict
        try:
            r = requests.get(url = self.base + "search", headers = self.headers, params = {"entity_type":"city",
                        "entity_id" : city, "cuisines":cuis})
            data = r.json()

            rest_index = data['restaurants']
            self.res_list = []
            self.res_dict = {}
            for i in rest_index:
                self.res_list.append(i['restaurant']['name'])
                self.res_dict[i['restaurant']['name'].lower()] = i['restaurant']
                # print(i['restaurant']['name'])

            # print(data)
            # print(data)
                # cuisine_ID =
        except IndexError:
            print("Invalid Query")

    def get_rest_info(self, name):
        return self.res_dict[name.lower()]['url']

    def allCuisines(self):
        allCuis = {}
        r = requests.get(url = self.base + "cuisines", headers = self.headers, params = {"city_id" : 306})
        data = r.json()
        # print(data)
        cus_index = data['cuisines']
        for i in cus_index:
            allCuis[i['cuisine']['cuisine_name']] = i['cuisine']['cuisine_id']
        return allCuis



# def main():
#
#     print("Enter City Name: ")
#     query = input()
#     if type(query) is not str:
#         raise Exception('Invalid Name Format')
#     else:
#         get_city_ID(query)
#
#     print("Type of Cuisine(s): ")
#     # print("*separate multiple cuisines by comma*")
#     cuisine = input()
#     if type(cuisine) is not str:
#         raise Exception('Invalid Name Format')
#     else:
#         get_cuisine(cuisine)
#
#     print('')
#     get_rest_list(city_ID, cuisine_ID)
#     print('')
#     print('Choose a Restaurant: ')
#     choice = input()
#     print(get_rest_info(choice))
#
#     # get_city_info()
# main()
