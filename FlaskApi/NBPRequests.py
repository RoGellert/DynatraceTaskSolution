from flask import Flask, request, jsonify
from flask_cors import CORS
import holidays
import datetime
import requests

#creating a server object
app = Flask(__name__)

#exposing server from access
CORS(app)

#creating a list of polish holidays
holidays_poland = holidays.PL(years=range(2001,2024))


def is_not_a_working_day(date):
    """
    Returns True if provided date is either a weekend or 
    a polish holiday and False otherwise
    """
    if (date.weekday() >= 5):
        return True
    
    if (date in holidays_poland):
        return True

    return False


@app.route('/average_exchange_rate', methods=['GET'])
def get_average_exchange_rate():
    """
    Returns an average exchange rate from Narodowy Bank Polski's
    API provided a currency code and a date
    
    - currency_code: code of a currency (etc: GBP)
    - date: required date in a format yyyy-mm-dd (etc: 2023-04-21)

    The output is a singular float 

    - If a day is not a working day returns "no data (weekend or holiday)"
    - In case currency code consists of 0 characters returns "check code input"
    - In case date is in incorrect format returns "check date input"
    - If server fails to fetch data returns 
      'server error, no such code or date available in the database'
    """
    #getting aruments from URL
    arguments = request.args

    currency_code = arguments.get('code')
    date = arguments.get('date')

    #making the code lowercase for the query to API to work properly
    currency_code = currency_code.lower()

    #checking if string with currency code is not 0
    if (len(currency_code) == 0):
        return jsonify('check code input')
    
    #checking the format of the date
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except:
        return jsonify('check date input')

    #checking if the day is the working day
    if (is_not_a_working_day(date)):
        return jsonify('no data (weekend or holiday)')
    
    #calling the API
    try:
        requested_data = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/' 
                                            + currency_code + '/' + str(date)
                                            + '?format=json').json()
    except:
        return jsonify('server error, no such code or date available in the database') 
    
    #extracting the exchange rate from the received data
    requested_average_exchange_rate = requested_data['rates'][0]['mid']
    
    return jsonify(requested_average_exchange_rate)


@app.route('/min_and_max_average_values', methods=['GET'])
def get_min_and_max_average_values():
    """
    Returns minimum and maximum average values from Narodowy Bank Polski's
    API provided a currency code and a number of last quotations
    
    - currency_code: code of a currency (etc: GBP)
    - last_quotations_num: number of last quotations <= 255 and > 0

    The output is an list containing min and max values

    - In case currency code consists of 0 characters returns ['check code input', 'check code input']
    - In case last_quotations_num is out of correct range returns ['check quotation number input', 'check quotation number input']
    - If server fails to fetch data returns 
      ["server error or currency code doesn't exist in the database", 
      "server error or currency code doesn't exist in the database"]
    """
    #getting aruments from URL
    arguments = request.args

    currency_code = arguments.get('code')
    last_quotations_num = arguments.get('last_quotations_num')

    #making the code lowercase for the query to API to work properly
    currency_code = currency_code.lower()

    #checking if string with currency code is not 0
    if (len(currency_code) == 0):
        return jsonify(['check code input', 'check code input'])
    
    #checking if last_quotations_num is in range
    if (int(last_quotations_num) < 1 or int(last_quotations_num) > 255):
        return jsonify(['check quotation number input', 'check quotation number input'])

    #calling the API
    try:
        requested_data = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/' 
                                            + currency_code + '/last/' + last_quotations_num
                                            + '?format=json').json()
    except:
        return jsonify(["server error or currency code doesn't exist in the database", 
                        "server error or currency code doesn't exist in the database"])
    
    #extracting the exchange rates, finding max and min
    list_of_average_exchange_rates = [values['mid'] for values in requested_data['rates']]
    min_average_exchange_rate = min(list_of_average_exchange_rates)
    max_average_exchange_rate = max(list_of_average_exchange_rates)

    return jsonify([min_average_exchange_rate, max_average_exchange_rate])


@app.route('/major_difference', methods=['GET'])
def get_major_difference():
    """
    Returns the major (which I have understood as maximum) difference between ask and bid values from 
    Narodowy Bank Polski's API provided a currency code and a number of last quotations
    
    - currency_code: code of a currency (etc: GBP)
    - last_quotations_num: number of last quotations <= 255 and > 0

    The output is a singular float 

    - In case currency code consists of 0 characters returns 'check code input'
    - In case last_quotations_num is out of correct range returns 'check quotation number input'
    - If server fails to fetch data returns 
      "server error or currency code doesn't exist in the database"
    """
     #getting aruments from URL
    arguments = request.args

    currency_code = arguments.get('code')
    last_quotations_num = arguments.get('last_quotations_num')

    #making the code lowercase for the query to API to work properly
    currency_code = currency_code.lower()

    #checking if string with currency code is not 0
    if (len(currency_code) == 0):
        return jsonify('check code input')
    
    #checking if last_quotations_num is in range
    if (int(last_quotations_num) < 1 or int(last_quotations_num) > 255):
        return jsonify('check quotation number input')

    #calling the API
    try:
        requested_data = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/' 
                                      + currency_code + '/last/' 
                                      + last_quotations_num
                                      + '?format=json').json()
    except:
        return jsonify("server error or currency code doesn't exist in the database")

    #creating an array of differences using map and calculating the biggest 
    list_of_ask_bid = [[values['ask'], values['bid']] for values in requested_data['rates']]
    list_of_ask_bid_differences = list(map(lambda x: x[0] - x[1], list_of_ask_bid))
    major_ask_bid_difference = max(list_of_ask_bid_differences)

    return jsonify(major_ask_bid_difference)
    
#running the server
app.run(host='0.0.0.0')
