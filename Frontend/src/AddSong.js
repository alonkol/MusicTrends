import React, { Component } from 'react';
import Button from "antd/es/button/button";
import Input from "antd/es/input/Input";
import {message} from "antd/lib/index";
import Cascader from "antd/es/cascader/index";
import CategoriesCascader from "./CategoriesCascader";
import { getParam } from './Utils.js';

class AddSong extends Component {

    constructor() {
        super();
        this.state = {
            category_id: null,
            artists_cascader_disabled: true,
            artists_for_category: [],
            artist_id: null,
            song_textarea_disabled: true
        }
    }

    handleCategoryChange = (value) => {
        this.setState({category_id: value});

        // get artists_for_category
        fetch("/api/artists_for_category/" + value)
            .then(results => results.json())
            .then(results => (this.setState({
                artists_for_category: results.results.map(artist =>
                    ({value: artist['artistName'], label: artist['artistName'], id: artist['artistID']}))
            })));

        this.setState({artists_cascader_disabled: false, song_textarea_disabled:true, artist_id: null});

    }

    handleArtistChange = (value, selectedOptions) => {
        const artist_id = selectedOptions[0]['id'];
        this.setState({artist_id: artist_id, song_textarea_disabled: false});
    }


    handleSubmit = (e) => {
        e.preventDefault();

        let song = document.forms["add-song"]["song"].value,
            artist = this.state.artist_id,
            category = this.state.category_id;

        // const key = getParam("key");
        const secretKey = 'abc';

        if (song === '') {
            message.error("Please enter the song's name");
        }
        else if (artist=== null) {
            message.error("No artist was chosen");
        }
        else if (category === null) {
            message.error("No category was chosen");
        }

        else {
            fetch("/api/songs/add?key=" + key + "&song=" + song + "&artist=" + artist + "&category=" + category)
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
                    <tbody>
                        <tr>
                            <td align="center" colSpan={4}>
                                Adding a new song is done by fetching data from <strong>Youtube</strong> and <strong>MusicMatch</strong>.
                            </td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td>Category:
                            </td>
                            <td >
                               <CategoriesCascader
                                width={'75%'}
                                handleChange={this.handleCategoryChange}
                                />
                            </td>
                            <td align="center" width="70">
                            Artist:
                            </td>
                            <td width="200"><Cascader
                            options={this.state.artists_for_category}
                            placeholder="Choose Artist"
                            showSearch
                            disabled={this.state.artists_cascader_disabled}
                            onChange={this.handleArtistChange}
                            />
                        </td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td width="100">
                                Song Name:
                            </td>
                            <td width="200">
                                <Input id={'song'} placeholder="Song Name" disabled={this.state.song_textarea_disabled}/>
                            </td>
                            <td colSpan={2} align={'center'}>
                                <Button
                                    type="primary"
                                    htmlType='submit'
                                    icon="plus-circle-o"
                                    size={'large'}
                                >Add Song</Button>
                            </td>
                        </tr>
                     </tbody>
                    </table>
                </form>
            </div>
        );
    }

}

export default AddSong;
