import { useState, useEffect } from 'react'
import './App.css'


function App() {
  // creating variables to store received data
  const [AverageExchangeRate, setAverageExchangeRate] = useState(0);
  const [MinRateValue, setMinRateValue] = useState(0);
  const [MaxRateValue, setMaxRateValue] = useState(0);
  const [MajorDifference, setMajorDifference] = useState(0);

  // creating variables to data to use in requests
  const [DateToReturn, setDateToReturn] = useState('2023-01-02');
  const [CodeToReturnFirst, setCodeToReturnFirst] = useState('GBP');
  const [CodeToReturnSecond, setCodeToReturnSecond] = useState('GBP');
  const [CodeToReturnThird, setCodeToReturnThird] = useState('GBP');
  const [LastQuotationsToReturnFirst, setLastQuotationsToReturnFirst] = useState(1);
  const [LastQuotationsToReturnSecond, setLastQuotationsToReturnSecond] = useState(1);

  // function to fetch average exchange rate from API
  const FetchAverageExchangeRate = () => {
    const fetchAdress =
      "http://localhost:5000/average_exchange_rate?code=" +
      CodeToReturnFirst +
      "&date=" +
      DateToReturn

    fetch(fetchAdress).then((res) =>
      res.json().then((data) => {
        setAverageExchangeRate(data);
      })
    );
  }

  // function to fetch min and max rates from API
  const FetchMinMaxRates = () => {
    const fetchAdress =
      "http://localhost:5000/min_and_max_average_values?code=" +
      CodeToReturnSecond +
      "&last_quotations_num=" +
      LastQuotationsToReturnFirst

    fetch(fetchAdress).then((res) =>
      res.json().then((data) => {
        setMinRateValue(data[0]);
        setMaxRateValue(data[1]);
      })
    );
  }

  // function to fetch major difference from API
  const FetchMajorDifference = () => {
    const fetchAdress =
      "http://localhost:5000//major_difference?code=" +
      CodeToReturnSecond +
      "&last_quotations_num=" +
      LastQuotationsToReturnSecond

    fetch(fetchAdress).then((res) =>
      res.json().then((data) => {
        setMajorDifference(data);
      })
    );
  }

  // functions to operate with events to change data displayed 

  const changeDate = (event) => {
    setDateToReturn(event.target.value);
  };
  
  const changeCodeToReturnFirst = (event) => {
    setCodeToReturnFirst(event.target.value);
  };
  
  const changeCodeToReturnSecond = (event) => {
    setCodeToReturnSecond(event.target.value);
  };
  
  const changeCodeToReturnThird = (event) => {
    setCodeToReturnThird(event.target.value);
  };
  
  const changeLastQuotationsToReturnFirst = (event) => {
    setLastQuotationsToReturnFirst(event.target.value);
  };
  
  const changeLastQuotationsToReturnSecond = (event) => {
    setLastQuotationsToReturnSecond(event.target.value);
  };

  //initial data fetching
  useEffect(() => FetchAverageExchangeRate(), []);
  useEffect(() => FetchMinMaxRates(), []);
  useEffect(() => FetchMajorDifference(), []);

  return (
    <div>
      <h1>
        A simple front-end for the internship task
      </h1>
      <div className='card'>
        <p>
        Returns an average exchange rate from Narodowy Bank Polski's
        API provided a currency code and a date
        </p>
        <div className='forms'>
          <form>
            <label>Date:
              <input type='date' value={DateToReturn} onChange={changeDate}/>
            </label>
          </form>
          <form>
            <label>Currency code:
              <input type='text' value={CodeToReturnFirst} onChange={changeCodeToReturnFirst}/>
            </label>
          </form>
        </div>
        <div className='results'>
          <label className='result_label'>
            Average exchange rate is : {AverageExchangeRate} 
          </label>
          <button className='refresh_button' onClick={FetchAverageExchangeRate}>REFRESH</button>
        </div>
      </div>
      <div className='card'>
        <p>
        Returns minimum and maximum average values from Narodowy Bank Polski's
        API provided a currency code and a number of last quotations
        </p>
        <div className='forms'>
          <form>
            <label>Number of last quotations:
              <input type='number' min='0' max="355" value={LastQuotationsToReturnFirst} onChange={changeLastQuotationsToReturnFirst}/>
            </label>
          </form>
          <form>
            <label>Currency code:
              <input type="text" value={CodeToReturnSecond} onChange={changeCodeToReturnSecond}/>
            </label>
          </form>
        </div>
        <div className='results'>
          <label className='result_label'>
            Min : {MinRateValue} 
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Max : {MaxRateValue} 
          </label>
          <button className='refresh_button' onClick={FetchMinMaxRates}>REFRESH</button>
        </div>
      </div>
      <div className='card'>
        <p>
        Returns the major difference between ask and bid values from 
        Narodowy Bank Polski's API provided a currency code and a number of last quotations
        </p>
        <div className='forms'>
          <form>
            <label>Number of last quotations:
              <input type='number' min='0' max="355" value={LastQuotationsToReturnSecond} onChange={changeLastQuotationsToReturnSecond}/>
            </label>
          </form>
          <form>
            <label>Currency code:
              <input type="text" value={CodeToReturnThird} onChange={changeCodeToReturnThird}/>
            </label>
          </form>
        </div>
        <div className='results'>
          <label className='result_label'>
            The major difference is : {MajorDifference}
          </label>
          <button className='refresh_button' onClick={FetchMajorDifference}>REFRESH</button>
        </div>
      </div>
      <h2>Roman Gellert 24.04.2023</h2>
    </div>
  )
}

export default App
