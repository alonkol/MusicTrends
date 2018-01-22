import React, { Component } from 'react';
import './App.css';
import TopList from "./TopList2";

const MAX_RESULTS_NUM = 20;

var categoryFilter = "?category=0";

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
        this.fetchAndUpdate("/api/words/top/", "topWords");
        this.fetchAndUpdate("/api/words/bottom/", "worstWords");
        this.fetchAndUpdate("/api/songs/likes/top/", "topLiked");
        this.fetchAndUpdate("/api/songs/dislikes/top/", "topDisliked");
        this.fetchAndUpdate("/api/songs/views/top/", "topViews");
        this.fetchAndUpdate("/api/songs/views/bottom/", "worstViews");
        this.fetchAndUpdate("/api/songs/wordscore/top/", "topWordScore");
        this.fetchAndUpdate("/api/songs/wordscore/bottom/", "worstWordScore");
        this.fetchAndUpdate("/api/songs/discussionscore/top/", "topDiscScore");
        this.fetchAndUpdate("/api/songs/viral_songs/top/", "topViralSongs");
        this.fetchAndUpdate("/api/songs/days_with_most_comments/top/", "topCommentedDays");
        this.fetchAndUpdate("/api/groupies/top/", "topGroupies");
        this.fetchAndUpdate("/api/artists/head_eaters/top/", "topHeadEaters");
        this.fetchAndUpdate("/api/artists/controversial/top/", "topControversial");

    }

    fetchAndUpdate = (endpoint, keyName) => {
        const _this = this;
        fetch(endpoint + MAX_RESULTS_NUM + categoryFilter)
                .then(this.handleErrors)
                .then(results => {
                    if (!results){
                        throw Error("Result object is null");
                    }

                    return results.json()
                })
                .then(resultsJson => {
                    this.dict = {}
                    this.dict[keyName] = Object.assign(_this.state[keyName], {items: resultsJson.results})
                    this.setState(this.dict);
                })
                .catch(console.log);
    }

    handleErrors = response => {
        if (!response.ok) {
            throw Error(response.statusText);
        }

        return response;
    }

    componentDidMount() {
        this.fetchResults();
    }
}

export default TrendsChart;
