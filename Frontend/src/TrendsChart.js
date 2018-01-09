import React, { Component } from 'react';
import './App.css';
import TopList from "./TopList2";

class TrendsChart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            topWords: {title: 'Top Words', items: []},
            numOfResults: props.numOfResults
        };
    }

    render() {
        return (
            <table>
                <tr>
                    <td><TopList title={this.state.topWords.title} items={this.state.topWords.items}/></td>
                    <td><TopList title={this.props.topSongs.title} items={this.props.topSongs.items}/></td>
                    <td><TopList title={this.props.topSongs.title} items={this.props.topSongs.items}/></td>
                </tr>
                <tr>
                    <td><TopList title={this.props.topSongs.title} items={this.props.topSongs.items}/></td>
                    <td><TopList title={this.props.topSongs.title} items={this.props.topSongs.items}/></td>
                    <td><TopList title={this.props.topSongs.title} items={this.props.topSongs.items}/></td>
                </tr>
            </table>
        );
    }

    componentDidMount() {
        // fetch categories

        // fetch top words
        fetch("/api/words/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topWords: Object.assign(this.state.topWords,
                    {items: results.results.map(word_record => word_record["word"])}
                )})));

    }
}

export default TrendsChart;
