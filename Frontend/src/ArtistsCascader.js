import React, { Component } from 'react';
import Cascader from "antd/es/cascader/index";

class ArtistsCascader extends Component {

    constructor() {
        super();
        this.state = {artists: []}
    }

    onChange = (value) => {
        this.props.handleChange(value[0]);
    }

    render() {
        return (
            <Cascader
                options={this.state.artists}
                placeholder="Choose Artist"
                showSearch={{matchInputWidth: false}}
                onChange={this.onChange}
            />
        );
    }

    componentDidMount() {
        fetch("/api/artists")
            .then(results => results.json())
            .then(results => (this.setState({artists: results.results.map(artist =>
                ({value: artist['artistName'], label: artist['artistName']}))})));
    }

}

export default ArtistsCascader;
