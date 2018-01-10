import React, { Component } from 'react';
import './App.css';
import Cascader from "antd/es/cascader/index";
import TextArea from "antd/es/input/TextArea";
import Button from "antd/es/button/button";

class UpdateSongData extends Component {

    constructor() {
        super();
        this.state = {}
    }

    render() {
        return (
            <div>
                <h2>Update Song Data</h2>
                <form>
                    <table>
                        <tr>
                            <td>Find Song:</td>
                            <td width={250}><Cascader
                                options={this.state.categories}
                                placeholder="Choose Artist"
                                showSearch /></td>
                            <td width={250}><Cascader
                                options={this.state.categories}
                                placeholder="Choose Song"
                                showSearch
                                disabled={true}/>
                            </td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td colspan="3"><TextArea rows={6} /></td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>
                                <Button type="primary" icon="youtube" size={'large'}>Update Youtube Data</Button>
                            </td>
                            <td>
                                <Button type="primary" icon="edit" size={'large'}>Update Lyrics</Button>
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

export default UpdateSongData;
