import React, { Component } from 'react';
import Cascader from "antd/es/cascader/index";
import Button from "antd/es/button/button";
import Input from "antd/es/input/Input";
import Icon from "antd/es/icon/index";

class AddSong extends Component {

    constructor() {
        super();
        this.state = {}
    }

    render() {
        return (
            <div>
                <h2>Add Song to Our Dataset</h2>
                <form>
                    <table>
                        <tr>
                            <td colSpan={4}>Adding a new song is done by fetching data from Youtube and MusicMatch.</td>
                        </tr>
                        <tr>
                            <br/>
                        </tr>
                        <tr>
                            <td>Song Name:
                            </td>
                            <td>
                                <Input placeholder="Song Name" />
                            </td>
                            <td>
                            Artist:
                            </td>
                            <td><Input
                                placeholder="Artist name"
                                prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
                            /></td>
                        </tr>
                        <tr>
                            <br/>
                        </tr>
                        <tr>
                            <td>Category:
                            </td>
                            <td width={250}>
                                <Input placeholder="Category" />
                            </td>
                            <td colSpan={2} align={'center'}>
                                <Button type="primary" icon="plus-circle-o" size={'large'}>Add Song</Button>
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

export default AddSong;
