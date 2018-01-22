import React, { Component } from 'react';
import './App.css';
import Input from "antd/es/input/Input";
import Button from "antd/es/button/button";
import { handleErrors } from './Utils.js';

class Search extends Component {

    constructor(props){
        super(props);

        this.state = {results: [], firstSearch: true};
    }

    render() {
        return (
            <div class="searchContent">
                <h3>Find a song by searching its lyrics!</h3>
                <Input
                    id="searchBox"
                    placeholder={"Search Lyrics..."}
                />
                <Button
                    onClick={this.handleSearchClick}
                    type="primary"
                    htmlType='submit'
                    size={'large'}
                >
                    Find Song
                </Button>

                <br />

                <div>{this.renderResults()}</div>

            </div>
        );
    }

    renderResults = () => {
        if (!this.state.firstSearch && this.state.results.length === 0){
            return "No results found";
        }

        return <ul>this.state.results.map(this.formatFunction)</ul>
    }

    formatFunction = (singleResult) => {
        return <li>singleResult</li>
    }

    handleSearchClick = () => {
        const text = document.getElementById('searchBox').value;
        fetch("/api/lyrics/search?text=" + text)
        .then(handleErrors)
        .then(results => results.json())
        .then(resultsJson => {
            this.setState({results: resultsJson.results, firstSearch: false});
        })
        .catch(console.log);
    }
}

export default Search;