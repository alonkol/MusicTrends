import React, { Component } from 'react';
import './App.css';
import UpdateSongData from "./UpdateSongData";

class Management extends Component {

    constructor() {
        super();
        this.state = {}
    }

    render() {
        return (
            <UpdateSongData/>
        )
        ;
    }

    componentDidMount() {

    }
}

export default Management;
