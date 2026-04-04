import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    setInterval(() => {
      fetch("http://localhost:8080/metrics")
        .then(res => res.json())
        .then(d => setData(d));
    }, 2000);
  }, []);

  return <div>Metrics Dashboard</div>;
}

export default App;