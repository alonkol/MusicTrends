import React, { Component } from 'react';
import './App.css';
import TopList from "./TopList2";

const MAX_RESULTS_NUM = 20;

var categoryFilter = "";

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
            numberOfResults: props.numberOfResults,

            selectedCategory: props.selectedCategory,
            selectedCategoryFilter: ""
        };
    }

    render() {
        return (
            <table>
                <tr>
                    <td><TopList title={this.state.topWords.title} items={this.state.topWords.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.worstWords.title} items={this.state.worstWords.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.topLiked.title} items={this.state.topLiked.items} numberOfResults={this.props.numberOfResults}/></td>
                </tr>
                <tr>
                    <td><TopList title={this.state.topDisliked.title} items={this.state.topDisliked.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.topViews.title} items={this.state.worstViews.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.topWordScore.title} items={this.state.topWordScore.items} numberOfResults={this.props.numberOfResults}/></td>
                </tr>
                <tr>
                    <td><TopList title={this.state.worstWordScore.title} items={this.state.worstWordScore.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.topDiscScore.title} items={this.state.topDiscScore.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.topGroupies.title} items={this.state.topGroupies.items} numberOfResults={this.props.numberOfResults}/></td>
                </tr>
                <tr>
                    <td><TopList title={this.state.topHeadEaters.title} items={this.state.topHeadEaters.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.topSameTextCouples.title} items={this.state.topSameTextCouples.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td><TopList title={this.state.topCommentedDays.title} items={this.state.topCommentedDays.items} numberOfResults={this.props.numberOfResults}/></td>
                </tr>
                <tr>
                    <td></td>
                    <td><TopList title={this.state.topControversial.title} items={this.state.topControversial.items} numberOfResults={this.props.numberOfResults}/></td>
                    <td></td>
                </tr>
            </table>
        );
    }


    componentWillReceiveProps(nextProps) {
        // filter changed
        if (this.props.selectedCategoryFilter != nextProps.selectedCategoryFilter) {
            categoryFilter = nextProps.selectedCategoryFilter;
            this.setState({
                selectedCategoryFilter: nextProps.selectedCategoryFilter,
                numberOfResults: nextProps.numberOfResults
            })

            console.log(nextProps.selectedCategoryFilter);
            this.fetchResults();
        }
    }

    fetchResults = () => {
        // fetch top words

        fetch("/api/words/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topWords: Object.assign(this.state.topWords,
                        {items: results.results}
                    )})));

        fetch("/api/words/bottom/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {worstWords: Object.assign(this.state.worstWords,
                        {items: results.results}
                    )})));

        // fetch top liked
        fetch("/api/songs/likes/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topLiked: Object.assign(this.state.topLiked,
                        {items: results.results}
                    )})));


        // fetch top disliked
        fetch("/api/songs/dislikes/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topDisliked: Object.assign(this.state.topDisliked,
                        {items: results.results}
                    )})));

        fetch("/api/songs/views/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topViews: Object.assign(this.state.topViews,
                        {items: results.results}
                    )})));

        fetch("/api/songs/views/bottom/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {worstViews: Object.assign(this.state.worstViews,
                        {items: results.results}
                    )})));

        fetch("/api/songs/wordscore/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topWordScore: Object.assign(this.state.topWordScore,
                        {items: results.results}
                    )})));

        fetch("/api/songs/wordscore/bottom/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {worstWordScore: Object.assign(this.state.worstWordScore,
                        {items: results.results}
                    )})));

        fetch("/api/songs/discussionscore/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topDiscScore: Object.assign(this.state.topDiscScore,
                        {items: results.results}
                    )})));

        fetch("/api/groupies/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topGroupies: Object.assign(this.state.topGroupies,
                        {items: results.results}
                    )})));

        fetch("/api/artists/head_eaters/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topHeadEaters: Object.assign(this.state.topHeadEaters,
                        {items: results.results}
                    )})));

        /*
        fetch("/api/artists/same_text_couples/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topSameTextCouples: Object.assign(this.state.topSameTextCouples,
                        {items: results.results}
                    )})));
*/
        fetch("/api/songs/days_with_most_comments/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topCommentedDays: Object.assign(this.state.topCommentedDays,
                        {items: results.results}
                    )})));

        fetch("/api/artists/controversial/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topControversial: Object.assign(this.state.topControversial,
                        {items: results.results}
                    )})));

    }

    componentDidMount() {
        this.fetchResults();
    }
}

export default TrendsChart;
