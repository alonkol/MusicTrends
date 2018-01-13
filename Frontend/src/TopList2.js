import React, { Component } from 'react';
import './App.css';

class TopList extends Component {

    constructor(props){
        super(props);

        this.state = {numberOfResults: props.numberOfResults};
    }

    render() {
        return (
            <div>
                <h2>{this.props.title}</h2>
                <ol>{this.props.items.slice(0, this.props.numberOfResults).map((item) => <li>{item['value'] + "\t" + item['count']}</li>)}</ol>
            </div>
        );
    }
}

export default TopList;
