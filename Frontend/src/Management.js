import React, { Component } from 'react';
import './App.css';
import UpdateSongData from "./UpdateSongData";
import Blacklist from "./Blacklist";

class Management extends Component {

    constructor() {
        super();
        this.state = {}
    }

    render() {
        return (
            <Blacklist/>
        )
        ;
    }

    componentDidMount() {

    }
}

export default Management;
