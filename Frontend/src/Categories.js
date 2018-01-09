import React, { Component } from 'react';

class Categories extends Component {

    constructor() {
        super();
        this.state = {categories: []}
    }

    render() {
        return (
            <div>
                {console.log(this.state.categories)}
            </div>
        );
    }


    componentDidMount() {
        fetch("/api/categories")
            .then(results => results.json())
            .then(results => (this.setState({categories: results.results})));
        /*
                    .then(results => console.log(results)
                    */
    }

    /*
    async componentDidMount() {
        const songs = await fetch("/api/categories")
            .then(results => results.json()).then(data => )
        console.log(songs)
        this.setState({songs})
    }
    */
}

export default Categories;
