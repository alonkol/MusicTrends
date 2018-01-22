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
            <table>

            <tr><td><h3>Find a song by searching its lyrics!</h3></td></tr>
            <tr><td><Input
                    id="searchBox"
                    placeholder={"Search Lyrics..."}
                /></td></tr>

                <tr><td><br /></td></tr>
                <tr><td align="center"><Button
                    onClick={this.handleSearchClick}
                    type="primary"
                    htmlType='submit'
                    size={'large'}
                >
                    Find Song
                </Button>
                </td></tr>
                <tr><td><br /></td></tr>
                <tr><td>
                <div class="songList">{this.renderResults()}</div>
                </td></tr>
            </table>
            </div>
        );
    }

    renderResults = () => {
        if (!this.state.firstSearch && this.state.results.length === 0){
            return "No results found";

        }

        return <ul>{this.state.results.map(this.formatFunction)}</ul>
    }

    formatFunction = (singleResult) => {
        return <li>{singleResult.songName}</li>
    }

    handleSearchClick = () => {
        const text = document.getElementById('searchBox').value;
        fetch("/api/lyrics/search?text=" + text)
        .then(handleErrors)
        .then(results => results.json())
        .then(results => {
            this.setState({results: results.results.map(song => ({songName: song['songName']})), firstSearch: false});
        })
        .catch(console.log);
    }
}

export default Search;