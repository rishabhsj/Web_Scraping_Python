import os
import json
import sys
from requests_html import HTMLSession


class WebScrape:

    def __init__(self, urls):

        try:
            if not os.path.exists('./Results/'):
                os.makedirs('./Results/')
        except Exception as exception:
            print(" \n Error - Json folder could not be created: {}\n ".format(exception))

        try:
            self.session = HTMLSession()
            self.run_all(urls)
        except Exception as exception:
            print("\n Error - session not started: {}\n".format(exception))
            sys.exit()

    @staticmethod
    def get_data(response):
        try:
            all_data = response.html.find('#site-content > div > div')
            all_data = all_data[0].text.splitlines()
            return all_data

        except Exception as exception:
            print("\n Web data not retrieved: {}\n".format(exception))

    @staticmethod
    def output_json(property_name):
        try:
            open(('Results/{}.json'.format(property_name)), 'wb')
        except Exception as exception:
            print("\n Output Json file could not be created: {}\n".format(exception))

    def property_name(self, all_data):
        try:
            property_name = all_data[0]
            self.output_json(property_name)
            return property_name
        except Exception as exception:
            print("\n Property Name not fetched: {}\n".format(exception))

    @staticmethod
    def property_type(all_data):
        try:
            type_index = [
                i for i,
                      str in enumerate(all_data)
                if 'hosted' in str
            ]
            type_index = int(type_index[0])
            property_type = all_data[type_index]

            return property_type
        except Exception as exception:
            print("\n Property type retrieved failed: {}\n".format(exception))

    @staticmethod
    def bedrooms(all_data):
        try:
            bed_index = [
                i for i,
                      str in enumerate(all_data)
                if 'bedroom' in str
            ]
            bed_index = int(bed_index[0])
            bedroom_num = all_data[bed_index]
            return bedroom_num
        except Exception as exception:
            print("\n Bedroom number retrieved failed: {}\n".format(exception))

    @staticmethod
    def bathrooms(all_data):
        try:
            bath_index = [
                i for i,
                      str in enumerate(all_data)
                if 'bathroom' in str
            ]
            bath_index = int(bath_index[0])
            bathroom_num = all_data[bath_index]
            return bathroom_num
        except Exception as exception:
            print("\n Bedroom number retrieved failed: {}\n".format(exception))

    @staticmethod
    def amenities(all_data):
        try:
            amenities_index = [
                i for i,
                      str in enumerate(all_data)
                if 'kitchen' in str
            ]
            amenities_index = int(amenities_index[0])
            amenities_list = all_data[amenities_index]
            return amenities_list
        except Exception as exception:
            print("\n Amenities list retrieved failed: {}\n".format(exception))

    def run_all(self, urls):
        try:
            for url in urls:
                response = self.session.get(url)
                property_dict = {}
                response.html.render(sleep=5, keep_page=True)

                info = self.get_data(response)
                property_name = self.property_name(info)
                property_type = self.property_type(info)
                bedrooms = self.bedrooms(info)
                bathrooms = self.bathrooms(info)
                amenities_list = self.amenities(info)

                property_dict["Property Name"] = property_name
                property_dict["Property Type"] = property_type
                property_dict["Number of Bedrooms"] = bedrooms
                property_dict["Number of Bathrooms"] = bathrooms
                property_dict["Amenities List"] = amenities_list

                print("\n Property Details: \n")
                for k, v in property_dict.items():
                    print(k, '-->', v)

                try:
                    with (open(('Results/{}.json'.format(property_name)), 'w')) as json_file:
                        json.dump(property_dict, json_file)
                except Exception as exception:
                    print("\n Failed parsing json to output file: {}\n".format(exception))

        except Exception as exception:
            print("\n Unable to access Url: {}\n".format(exception))
            sys.exit()
