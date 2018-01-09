import React, { Component } from 'react';
import './App.css';
import IntegerStep from "./IntegerStep";
import { Cascader } from 'antd';
import Search from "antd/es/input/Search";
import Checkbox from "antd/es/checkbox/Checkbox";

class FilterSection extends Component {

    constructor() {
        super();
        this.state = {categories: []}
    }

    render() {
        return (
            <div>
                <h1>Filters</h1>
                <form>
                    <table>
                        <tr>
                            <td width={250}><Checkbox onChange={checkboxOnChange} />  Category</td>
                            <td width={250}><Cascader
                                options={this.state.categories}
                                onChange={categoryCascaderOnChange()}
                                placeholder="Please select"
                                showSearch /></td>
                        </tr>
                        <tr>
                            <td><Checkbox onChange={checkboxOnChange} />  Artist</td>
                            <td><Search
                                placeholder="input search text"
                                onSearch={value => console.log(value)}
                                enterButton
                            /></td>
                        </tr>
                        <tr>
                            <td>Number of results</td>

                            <td><IntegerStep /></td>
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

function categoryCascaderOnChange(value, selectedOptions) {
    console.log(value, selectedOptions);
}

function checkboxOnChange(e) {
    console.log(`checked = ${e.target.checked}`);
}

export default FilterSection;
