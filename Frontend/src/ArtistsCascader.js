import React, { Component } from 'react';
import Cascader from "antd/es/cascader/index";

class ArtistsCascader extends Component {

    constructor() {
        super();
        this.state = {artists: []}
    }

    onChange = (value, selectedOptions) => {
        this.props.handleChange(selectedOptions[0]['id']);
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
                ({value: artist['artistName'], label: artist['artistName'], id: artist['artistID']}))})));
    }

}

export default ArtistsCascader;
