import React, { Component } from 'react';
import './App.css';
import TopList from "./TopList2";

class TrendsChart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            topWords: {title: 'Top Words', items: []},
            worstWords: {title: 'Worst Words', items: []},
            topLiked: {title: 'Top Liked', items: []},
            topDisliked: {title: 'Top Disliked', items: []},
            topViews: {title: 'Top Views', items: []},
            worstViews: {title: 'Worst Views', items: []},
            topWordScore: {title: 'Top Word Score', items: []},
            worstWordScore: {title: 'Worst Word Score', items: []},
            topDiscScore: {title: 'Top Discussed', items: []},
            topGroupies: {title: 'Top Groupies', items: []},
            topHeadEaters: {title: 'Top Head Eaters', items: []},
            topSameTextCouples: {title: 'Top text couples', items: []},
            topCommentedDays: {title: 'Top Commented Days', items: []},
            topControversial: {title: 'Top Controversial', items: []},
            numOfResults: props.numOfResults
        };
    }

    render() {
        return (
            <table>
                <tr>
                    <td><TopList title={this.state.topWords.title} items={this.state.topWords.items}/></td>
                    <td><TopList title={this.state.worstWords.title} items={this.state.worstWords.items}/></td>
                    <td><TopList title={this.state.topLiked.title} items={this.state.topLiked.items}/></td>
                </tr>
                <tr>
                    <td><TopList title={this.state.topDisliked.title} items={this.state.topDisliked.items}/></td>
                    <td><TopList title={this.state.topViews.title} items={this.state.worstViews.items}/></td>
                    <td><TopList title={this.state.topWordScore.title} items={this.state.topWordScore.items}/></td>
                </tr>
                <tr>
                    <td><TopList title={this.state.worstWordScore.title} items={this.state.worstWordScore.items}/></td>
                    <td><TopList title={this.state.topDiscScore.title} items={this.state.topDiscScore.items}/></td>
                    <td><TopList title={this.state.topGroupies.title} items={this.state.topGroupies.items}/></td>
                </tr>
                <tr>
                    <td><TopList title={this.state.topHeadEaters.title} items={this.state.topHeadEaters.items}/></td>
                    <td><TopList title={this.state.topSameTextCouples.title} items={this.state.topSameTextCouples.items}/></td>
                    <td><TopList title={this.state.topCommentedDays.title} items={this.state.topCommentedDays.items}/></td>
                </tr>
                <tr>
                    <td></td>
                    <td><TopList title={this.state.topControversial.title} items={this.state.topControversial.items}/></td>
                    <td></td>
                </tr>
            </table>
        );
    }

    fetchResults = () => {
        /*
        // fetch top words
        fetch("/api/words/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topWords: Object.assign(this.state.topWords,
                        {items: results.results}
                    )})));

        fetch("/api/words/bottom/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {worstWords: Object.assign(this.state.worstWords,
                        {items: results.results}
                    )})));

        // fetch top liked
        fetch("/api/songs/likes/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topLiked: Object.assign(this.state.topLiked,
                        {items: results.results}
                    )})));

        // fetch top disliked
        fetch("/api/songs/dislikes/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topDisliked: Object.assign(this.state.topDisliked,
                        {items: results.results}
                    )})));

        fetch("/api/songs/views/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topViews: Object.assign(this.state.topViews,
                        {items: results.results}
                    )})));

        fetch("/api/songs/views/bottom/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {worstViews: Object.assign(this.state.worstViews,
                        {items: results.results}
                    )})));

        fetch("/api/songs/wordscore/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topWordScore: Object.assign(this.state.topWordScore,
                        {items: results.results}
                    )})));

        fetch("/api/songs/wordscore/bottom/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {worstWordScore: Object.assign(this.state.worstWordScore,
                        {items: results.results}
                    )})));

        fetch("/api/songs/discussionscore/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topDiscScore: Object.assign(this.state.topDiscScore,
                        {items: results.results}
                    )})));

        fetch("/api/songs/groupies/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topGroupies: Object.assign(this.state.topGroupies,
                        {items: results.results}
                    )})));

        fetch("/api/songs/head_eaters/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topHeadEaters: Object.assign(this.state.topHeadEaters,
                        {items: results.results}
                    )})));

        fetch("/api/songs/same_text_couples/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topSameTextCouples: Object.assign(this.state.topSameTextCouples,
                        {items: results.results}
                    )})));

        fetch("/api/songs/days_with_most_comments/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topCommentedDays: Object.assign(this.state.topCommentedDays,
                        {items: results.results}
                    )})));

        fetch("/api/songs/controversial/top/" + this.state.numOfResults)
            .then(results => results.json())
            .then(results => (this.setState(
                {topControversial: Object.assign(this.state.topControversial,
                        {items: results.results}
                    )})));
                    */
    }

    componentDidMount() {
        this.fetchResults();
    }
}

export default TrendsChart;
