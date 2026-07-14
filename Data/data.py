# this one gets the data from  mangodb aka the discord messages and it will clean it up and make sure it can be used as training mod
## since the data is getting pulled from a database we will need to use pymongo to connect to the database and get the data
from pymongo import MongoClient
from dotenv import env
def get_data():
    return 

def clean_data(data):
    # clean the data here
    return data


def prepare_data():
    data = get_data()
    cleaned_data = clean_data(data)
    return cleaned_data

def save_data(data):
    # save the data to a file or database
    pass


def main():
    get_data()
    prepared_data = prepare_data()
    save_data(prepared_data)


if __name__ == "__main__":

    main()

