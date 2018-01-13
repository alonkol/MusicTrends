import React, { Component } from 'react';
import './App.css';
import IntegerStep from "./IntegerStep";
import { Cascader } from 'antd';
import Search from "antd/es/input/Search";
import Checkbox from "antd/es/checkbox/Checkbox";
import Switch from "antd/es/switch/index";

class FilterSection extends Component {

    constructor() {
        super();
        this.state = {categories: [],
        selectedCategory: null}
    }

    categoryCascaderOnChange = (value, selectedOptions) => {
        this.setState({selectedCategory: selectedOptions[0].id});
        this.props.handleCategoryChange(selectedOptions[0].id);
    }

    sliderOnChange = (value) => {
        console.log(value);
        this.props.handleSliderChange(value);
    }

    switchOnChange = (value) => {
        this.props.handleSwitchChange(value);
    }

    render() {
        return (
            <div>
                <h2>Filters</h2>
                <form>
                    <table>
                        <tr>
                            <td width={80}><Switch onChange={this.switchOnChange} /></td>
                            <td width={150}>
                                Category</td>
                            <td width={212}><Cascader
                                options={this.state.categories}
                                onChange={this.categoryCascaderOnChange}
                                placeholder="Please select"
                                showSearch /></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>Number of Results</td>

                            <td><IntegerStep onChange={this.sliderOnChange} /></td>
                        </tr>
                    </table>
                </form>
            </div>
        );
    }

    componentDidMount() {

        // fetch categories

        fetch("/api/categories")
            .then(results => results.json())
            .then(results => (this.setState({categories: results.results.map(category =>
                ({value: category['name'], label: category['name'], id: category['id']}))})));
    }
}

function countryCascaderOnChange(value, selectedOptions) {
    console.log(value, selectedOptions);
}

export default FilterSection;
