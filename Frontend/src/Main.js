import React, { Component } from 'react';
import './App.css';
import topSongs from './api/data.json';
import TrendsChart from "./TrendsChart";
import FilterSection from "./FilterSection";

class Main extends Component {
    render() {
        return (
            <div align="center">
                <FilterSection/>
                <br/>
                <br/>
                <TrendsChart topSongs={topSongs} numOfResults={5}></TrendsChart>
            </div>
        );
    }

}

export default Main;
