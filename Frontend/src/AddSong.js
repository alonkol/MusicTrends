import React, { Component } from 'react';
import Cascader from "antd/es/cascader/index";
import Button from "antd/es/button/button";
import Input from "antd/es/input/Input";
import Icon from "antd/es/icon/index";
import {message} from "antd/lib/index";

class AddSong extends Component {

    constructor() {
        super();
        this.state = {}
    }

    handleSubmit = (e) => {
        e.preventDefault();

        let song = document.forms["add-song"]["song"].value,
            artist = document.forms["add-song"]["artist"].value,
            category = document.forms["add-song"]["category"].value;

        if (song === '') {
            message.error("Please enter the song's name");
        }
        else if (artist=== '') {
            message.error("Please enter the artist's name");
        }
        else if (category === '') {
            message.error("Please enter the category's name");
        }

        else {
            fetch("/api/songs/add?key=&song=" + song + "&artist=" + artist + "&category=" + category)
                .then(result => result.json())
                .then(result => {
                    if (result['success'] === true) {
                        message.success('The song was added.');
                    }

                    else {
                        message.error('An error occurred.');
                    }
                });
        }

    }

    render() {
        return (
            <div>
                <h2>Add Song to Our Dataset</h2>
                <form name="add-song" onSubmit={this.handleSubmit}>
                    <table>
                        <tr>
                            <td align="center" colSpan={4}>
                                Adding a new song is done by fetching data from <strong>Youtube</strong> and <strong>MusicMatch</strong>.
                            </td>
                        </tr>
                        <tr>
                            <br/>
                        </tr>
                        <tr>
                            <td width="100">
                                Song Name:
                            </td>
                            <td width="200">
                                <Input id={'song'} placeholder="Song Name" />
                            </td>
                            <td align="center" width="70">
                            Artist:
                            </td>
                            <td width="200"><Input
                                id={'artist'}
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
                            <td >
                                <Input
                                    placeholder="Category"
                                    id={'category'}
                                />
                            </td>
                            <td colSpan={2} align={'center'}>
                                <Button
                                    type="primary"
                                    htmlType='submit'
                                    icon="plus-circle-o"
                                    size={'large'}
                                    onClick={this.addSong}
                                >Add Song</Button>
                            </td>
                        </tr>
                    </table>
                </form>
            </div>
        );
    }

}

export default AddSong;
