import React, { useState, useEffect } from 'react';

function App() {
  const [responseData, setResponseData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = () => {
    fetch('http://127.0.0.1:5000/gpt_powered')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setResponseData(data))
      .catch(error => console.error('Error fetching data:', error));
  };

  return (
    <div>
      {responseData ? (
        <h1>{responseData.message}</h1>
      ) : (
        <h1>Loading...</h1>
      )}
    </div>
  );
}

export default App;
