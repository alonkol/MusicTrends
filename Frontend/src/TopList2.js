import React, { Component } from 'react';
import './App.css';

class TopList extends Component {

    render() {
        return (
            <div>
                <h2>{this.props.title}</h2>
                <ol>{this.props.items.map((item) => <li>{item['value'] + item['count']}</li>)}</ol>
            </div>
        );
    }
}

export default TopList;
