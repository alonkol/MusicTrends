import React, { Component } from 'react';
import Cascader from "antd/es/cascader/index";
import Button from "antd/es/button/button";

class Blacklist extends Component {

    constructor() {
        super();
        this.state = {}
    }

    render() {
        return (
            <div>
                <h2>Black List</h2>
                <form>
                    <table>
                        <tr>
                            <td colSpan={3}>Blacklisting an artist will <b>remove</b> him from the application. Please choose artist:</td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td colSpan={3} width={250}><Cascader
                                options={this.state.categories}
                                placeholder="Choose Artist"
                                showSearch /></td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td colSpan={3} align={'center'}>
                                <Button type="danger" icon="delete" size={'large'}>Blacklist Artist</Button>
                            </td>
                        </tr>
                    </table>
                </form>
            </div>
        );
    }


    componentDidMount() {

    }

}

export default Blacklist;
