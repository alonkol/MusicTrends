import React, { Component } from 'react';
import './App.css';
import Input from "antd/es/input/Input";


class Search extends Component {

    render() {
        return (
            <div class="searchContent">
                <h3>Find a song by searching its lyrics!</h3>
                <Input placeholder={"Search Lyrics..."} />
            </div>
        );
    }
}

export default Search;