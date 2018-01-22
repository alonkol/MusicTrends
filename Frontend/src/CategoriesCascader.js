import React, { Component } from 'react';
import Cascader from "antd/es/cascader/index";

class CategoriesCascader extends Component {

    constructor() {
        super();
        this.state = {categories: []}
    }

    onChange = (value, selectedOptions) => {
        this.props.handleChange(selectedOptions[0]['id']);
    }

    render() {
        return (
            <Cascader
                options={this.state.categories}
                placeholder="Choose Category"
                showSearch={{matchInputWidth: false}}
                onChange={this.onChange}
                matchInputWidth={true}
                style={{ width: this.props.width }}
            />
        );
    }

    componentDidMount() {
        fetch("/api/categories")
            .then(results => results.json())
            .then(results => (this.setState({categories: results.results.map(category =>
                ({value: category['categoryName'], label: category['categoryName'], id: category['categoryID']}))})));
    }

}

export default CategoriesCascader;
