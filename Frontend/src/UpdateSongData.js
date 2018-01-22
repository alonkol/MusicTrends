import React, { Component } from 'react';
import './App.css';
import Cascader from "antd/es/cascader/index";
import TextArea from "antd/es/input/TextArea";
import Button from "antd/es/button/button";
import ArtistsCascader from "./ArtistsCascader";
import { message } from "antd";
import { getParam } from './Utils.js';


class UpdateSongData extends Component {

    constructor() {
        super();
        this.state = {
            artist_id: null,
            songs_cascader_disabled: true,
            songs_for_artist: [],
            song_id: null,
            lyrics_textarea_disabled: true
        }
    }

    handleArtistChange = (value) => {
        this.setState({artist_id: value});

        // get songs for artist
        fetch("/api/songs_for_artist/" + value)
            .then(results => results.json())
            .then(results => (this.setState({
                songs_for_artist: results.results.map(song =>
                    ({value: song['songName'], label: song['songName'], id: song['songID']}))
            })));

        this.setState({songs_cascader_disabled: false});
    }

    handleSongChange = (value, selectedOptions) => {
        const song_id = selectedOptions[0]['id'];
        this.setState({song_id: song_id, lyrics_textarea_disabled: false});

        // get lyrics for song
        fetch("/api/lyrics/get?song=" + song_id)
            .then(results => results.json())
            .then(results => (document.getElementById('lyrics').value = dbNewlineRepair(results.results[0]['lyrics'])));
    }

    handleUpdateLyricsSubmit = () => {
        const key = getParam("key");
        const lyrics = document.getElementById('lyrics').value,
            song_id = this.state.song_id;

        fetch("/api/lyrics/update?key=" + key + "&song=" + song_id + "&lyrics=" + lyrics)
            .then(result => result.json())
            .then(result => {
                if (result['success'] === true) {
                    message.success('The lyrics were updated.');
                }

                else {
                    message.error('An error occurred.');
                }
            });
    }

    handleUpdateYoutubeSubmit = () => {
        const key = getParam("key");
        const song_id = this.state.song_id;

        fetch("api/youtube/update?key=" + key + "&song=" + song_id)
            .then(result => result.json())
            .then(result => {
                if (result['success'] === true) {
                    message.success('The data was updated.');
                }

                else {
                    message.error(result['message']);
                }
            });
    }

    render() {
        return (
            <div>
                <h2>Update Song Data</h2>
                <table>
                <tbody>
                    <tr>
                        <td align="center" width={250}>
                            <ArtistsCascader
                                width={'75%'}
                                handleChange={this.handleArtistChange}
                            />
                        </td>
                        <td align="center" width={250}><Cascader
                            options={this.state.songs_for_artist}
                            placeholder="Choose Song"
                            showSearch
                            disabled={this.state.songs_cascader_disabled}
                            onChange={this.handleSongChange}
                        />
                        </td>
                    </tr>
                    <tr>
                        <td><br/></td>
                    </tr>
                    <tr>
                        <td colSpan="2">
                                <TextArea
                                    rows={6}
                                    disabled={this.state.lyrics_textarea_disabled}
                                    id='lyrics'
                                />
                        </td>
                    </tr>
                    <tr>
                        <td><br/></td>
                    </tr>
                    <tr>
                        <td align="right">
                            <Button
                                type="primary"
                                htmlType='submit'
                                icon="youtube"
                                size={'large'}
                                value='update-youtube-data'
                                onClick={this.handleUpdateYoutubeSubmit}
                            >
                                Update Youtube Data
                            </Button>
                        </td>
                        <td align="center">
                            <Button
                                type="primary"
                                htmlType='submit'
                                icon="edit"
                                size={'large'}
                                value='update-lyrics'
                                onClick={this.handleUpdateLyricsSubmit}
                            >
                                Update Lyrics
                            </Button>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        );
    }
}

function dbNewlineRepair(text) {
    return text.split("\\n").join("\n");
}

export default UpdateSongData;
