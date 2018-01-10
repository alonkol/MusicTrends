import React, { Component } from 'react';
import './App.css';
import UpdateSongData from "./UpdateSongData";
import Blacklist from "./Blacklist";
import AddSong from "./AddSong";

class Management extends Component {

    constructor() {
        super();
        this.state = {}
    }

    render() {
        return (
            <AddSong/>
        )
        ;
    }

    componentDidMount() {

    }
}

export default Management;
