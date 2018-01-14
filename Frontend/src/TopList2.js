import React, { Component } from 'react';
import './App.css';

class TopList extends Component {

    constructor(props){
        super(props);

        this.state = {numberOfResults: props.numberOfResults};
    }

    render() {
        return (
            <div class="singleList">
                <h2>{this.props.title}</h2>
                <h4>{this.props.description}</h4>
                <ol>{this.props.items.slice(0, this.props.numberOfResults).map(this.formatFunction)}</ol>
            </div>
        );
    }

    formatFunction(item){
        const test = item['value']

        return <li>{item['value'] + "\t" + item['count']}</li>;
    }
}

export default TopList;
