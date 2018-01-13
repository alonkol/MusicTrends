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
    }

}

export default Categories;
