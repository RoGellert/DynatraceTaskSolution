import requests

#testing query 1
class TestGetAverageExchange:
    def test_received_data1(self):
        correct_answer = 5.3515 #correct data

        currency_code = 'GBP' #correct code
        date = '2023-01-09' #working day

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


    def test_received_data2(self):
        correct_answer = 5.2768 #correct data

        currency_code = 'GBP' #correct code
        date = '2023-01-02' #working day

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


    def test_received_data3(self):
        correct_answer = 3.1881 #correct data

        currency_code = 'CAD' #correct code
        date = '2022-01-03' #working day

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


    def test_holiday(self):
        correct_answer = 'no data (weekend or holiday)' #correct response

        currency_code = 'GBP' #correct code
        date = '2023-01-06' #holiday

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


    def test_weekend(self):
        correct_answer = 'no data (weekend or holiday)' #correct response

        currency_code = 'GBP' #correct code
        date = '2023-01-07' #weekend

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


    def test_error_1(self):
        correct_answer = 'server error, no such code or date available in the database' #correct response
        
        currency_code = 'GBPAADSAD' #incorrect code
        date = '2023-01-05' #working day

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


    def test_error_2(self):
        correct_answer = 'server error, no such code or date available in the database' #correct response

        currency_code = 'GBP' #correct code
        date = '2025-01-07' #day not existing in the database

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


    def test_error_3(self):
        correct_answer = 'check code input' #correct response

        currency_code = '' #empty code
        date = '2023-01-06' #holiday

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer

    
    def test_error_4(self):
        correct_answer = 'check code input' #correct response

        currency_code = '' #empty code
        date = '2023-01-03' #workday

        received_data = requests.get('http://153.19.209.27:5000/average_exchange_rate?' 
                                            + 'code=' + currency_code + '&date=' + date
                                            ).json()
        
        assert received_data == correct_answer


#testing query 2
class TestGetMinMaxValues:
    def test_error1(self):
        correct_answer = ['check code input', 'check code input'] #correct response

        currency_code = '' #empty code
        last_quotations_num = 1 #correct quotations

        received_data = requests.get('http://153.19.209.27:5000/min_and_max_average_values?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer

    
    def test_error2(self):
        correct_answer = ['check quotation number input', 'check quotation number input'] #correct data

        currency_code = 'GBP' #correct code
        last_quotations_num = 0 #quotations out of range

        received_data = requests.get('http://153.19.209.27:5000/min_and_max_average_values?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer


    def test_error3(self):
        correct_answer = ['check quotation number input', 'check quotation number input'] #correct data

        currency_code = 'GBP' #correct code
        last_quotations_num = 256 #quotations out of range

        received_data = requests.get('http://153.19.209.27:5000/min_and_max_average_values?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer


    def test_error4(self):
        correct_answer = ["server error or currency code doesn't exist in the database", 
                        "server error or currency code doesn't exist in the database"] #correct data

        currency_code = 'GBPasd' #incorrect code
        last_quotations_num = 253 #quotations in range

        received_data = requests.get('http://153.19.209.27:5000/min_and_max_average_values?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer


#testing query 3
class TestMajorDifference:
    def test_error1(self):
        correct_answer = 'check code input' #correct response

        currency_code = '' #empty code
        last_quotations_num = 1 #correct quotations

        received_data = requests.get('http://153.19.209.27:5000/major_difference?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer

    
    def test_error2(self):
        correct_answer = 'check quotation number input' #correct response

        currency_code = 'GBP' #correct code
        last_quotations_num = 0 #quotations out of range

        received_data = requests.get('http://153.19.209.27:5000/major_difference?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer


    def test_error3(self):
        correct_answer = 'check quotation number input' #correct response

        currency_code = 'GBP' #correct code
        last_quotations_num = 256 #quotations out of range

        received_data = requests.get('http://153.19.209.27:5000/major_difference?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer


    def test_error4(self):
        correct_answer = "server error or currency code doesn't exist in the database" #correct response

        currency_code = 'GBPasd' #incorrect code
        last_quotations_num = 253 #quotations in range

        received_data = requests.get('http://153.19.209.27:5000/major_difference?' 
                                            + 'code=' + currency_code + '&last_quotations_num=' + str(last_quotations_num)
                                            ).json()
        
        assert received_data == correct_answer