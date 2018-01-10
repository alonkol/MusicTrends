import React, { Component } from 'react';
import './App.css';
import Main from "./Main";
import 'antd/dist/antd.css';

class App extends Component {
  render() {
    return (

      <div className="App">
          <Main/>
      </div>
        /*
        <header className="App-header">
            <img src={require("./images/logo.jpg")} alt="logo" width="30%"/>
        </header>
        <p className="App-intro">
            <Main/>
        </p>
      </div>
        */
    );
  }
}

export default App;
