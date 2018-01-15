import React, { Component } from 'react';
import Button from "antd/es/button/button";
import ArtistsCascader from "./ArtistsCascader";
import { message } from "antd";
import { getParam } from './Utils.js';


class Blacklist extends Component {


    constructor() {
        super();
        this.state = {artist: null}
    }

    handleChange = (value) => {
        this.setState({
            artist: value
        });
    }

    onClick = () => {
        const key = getParam("key");

        if (this.state.artist === null) {
            message.error('No artist has been chosen');
        }

        else {
            fetch("/api/blacklist_artist?key=" + key + "&artist=" + this.state.artist)
                .then(result => result.json())
                .then(result => {
                    if (result['success'] === true) {
                        message.success('Artist was blacklisted.');
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
                <h2>Blacklist</h2>
                <form>
                    <table>
                        <tr>
                            <td colSpan={3}>Blacklisting an artist will <b>remove</b> him from the application. Please choose artist:</td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td align="center" colSpan={3} width={250}>
                                <ArtistsCascader
                                    width={'80%'}
                                    handleChange={this.handleChange}
                                />
                            </td>
                        </tr>
                        <tr>
                            <td><br /></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td colSpan={3} align={'center'}>
                                <Button type="danger" icon="delete" size={'large'} onClick={this.onClick}>Blacklist Artist</Button>
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
