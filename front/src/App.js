import React from 'react';
import './App.css';
import TweetsHour from './components/TweetsHour'
import Followes from './components/Followers'

function App() {
  return (
    <div className="App">
      <div className="container">
      <h1>Twitter Collect Data</h1>
      <Followes></Followes>
      <div className="divider"></div>
      <TweetsHour></TweetsHour>
      <div className="divider"></div>
      </div>
    </div>
  );
}

export default App;
