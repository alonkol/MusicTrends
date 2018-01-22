import React, { Component } from 'react';
import './App.css';
import IntegerStep from "./IntegerStep";
import { Cascader } from 'antd';

class FilterSection extends Component {

    constructor() {
        super();
        this.state = {categories: [], selectedCategory: 0}
    }

    categoryCascaderOnChange = (value, selectedOptions) => {
        this.setState({selectedCategory: selectedOptions[0].id});
        this.props.handleCategoryChange(selectedOptions[0].id);
    }

    sliderOnChange = (value) => {
        console.log(value);
        this.props.handleSliderChange(value);
    }

    render() {
        return (
            <div>
                <h2>Filters</h2>
                <form>
                    <table>
                    <tbody>
                        <tr>
                            <td width={150}>
                                Category</td>
                            <td width={212}><Cascader
                                options={this.state.categories}
                                onChange={this.categoryCascaderOnChange}
                                placeholder="Please select"
                                showSearch /></td>
                        </tr>
                        <tr>
                            <td>Number of Results</td>
                            <td><IntegerStep onChange={this.sliderOnChange} /></td>
                        </tr>
                        </tbody>
                    </table>
                </form>
            </div>
        );
    }

    componentDidMount() {

        // fetch categories
        fetch("/api/categories")
            .then(results => results.json())
            .then(results => {
                var result_array = [({value: 'All', label: 'All', id: 0})]
                results.results.forEach(function(category) {
                    result_array.push({value: category['categoryName'], label: category['categoryName'], id: category['categoryID']});
                });
                this.setState({categories: result_array});
            });
    }
}

export default FilterSection;
