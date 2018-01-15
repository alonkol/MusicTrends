import React, { Component } from 'react';
import './App.css';
import TopList from "./TopList2";

const MAX_RESULTS_NUM = 20;

var categoryFilter = "";

class TrendsChart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            topWords: {title: 'Common Words', description: 'The most commonly used words', items: []},
            worstWords: {title: 'Rare Words', description: 'The most rarely used words', items: []},
            topLiked: {title: 'Most Liked', description: 'Songs with the highest amount of likes', items: []},
            topDisliked: {title: 'Most Disliked', description: 'Songs with the highest amount of dislikes', items: []},
            topViews: {title: 'Most Viewed', description: 'Songs with the highest amount of views', items: []},
            worstViews: {title: 'Least Viewed', description: 'Songs with the lowest amount of views', items: []},
            topWordScore: {title: 'Sophisticated', description: 'Songs with rich vocabulary in its lyrics', items: []},
            worstWordScore: {title: 'Dumb', description: 'Songs with poor vocabulary in its lyrics', items: []},
            topDiscScore: {title: 'Smart Fans', description: 'Songs with rich vocabulary in its Youtube video comments', items: []},
            topGroupies: {title: 'Groupies', description: 'These people comment on tons of videos by their favorite artist', items: []},
            topHeadEaters: {title: 'Head Eaters', description: 'Artists who write really long texts', items: []},
            topViralSongs: {title: 'Viral Songs', description: 'Songs which their comments are most liked', items: []},
            topCommentedDays: {title: 'Comment Timing', description: 'Days of the week with most Youtube comments', items: []},
            topControversial: {title: 'Controversial Artists', description: 'Popular artists who are also disliked by many', items: []},
            numberOfResults: props.numberOfResults,

            selectedCategory: props.selectedCategory,
            selectedCategoryFilter: ""
        };
    }

    render() {
        return (
        <div>
            <TopList title={this.state.topWords.title} description={this.state.topWords.description} items={this.state.topWords.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.worstWords.title} description={this.state.worstWords.description} items={this.state.worstWords.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topWordScore.title} description={this.state.topWordScore.description} items={this.state.topWordScore.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.worstWordScore.title} description={this.state.worstWordScore.description} items={this.state.worstWordScore.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topDiscScore.title} description={this.state.topDiscScore.description} items={this.state.topDiscScore.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topGroupies.title} description={this.state.topGroupies.description} items={this.state.topGroupies.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topHeadEaters.title} description={this.state.topHeadEaters.description} items={this.state.topHeadEaters.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topViralSongs.title} description={this.state.topViralSongs.description} items={this.state.topViralSongs.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topCommentedDays.title} description={this.state.topCommentedDays.description} items={this.state.topCommentedDays.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topControversial.title} description={this.state.topControversial.description} items={this.state.topControversial.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topLiked.title} description={this.state.topLiked.description} items={this.state.topLiked.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topDisliked.title} description={this.state.topDisliked.description} items={this.state.topDisliked.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.topViews.title} description={this.state.topViews.description} items={this.state.topViews.items} numberOfResults={this.props.numberOfResults}/>
            <TopList title={this.state.worstViews.title} description={this.state.worstViews.description} items={this.state.worstViews.items} numberOfResults={this.props.numberOfResults}/>
        </div>
        );
    }


    componentWillReceiveProps(nextProps) {
        // filter changed
        if (this.props.selectedCategoryFilter !== nextProps.selectedCategoryFilter) {
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

        fetch("/api/songs/viral_songs/top/" + MAX_RESULTS_NUM + categoryFilter)
            .then(results => results.json())
            .then(results => (this.setState(
                {topViralSongs: Object.assign(this.state.topViralSongs,
                        {items: results.results}
                    )})));

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
