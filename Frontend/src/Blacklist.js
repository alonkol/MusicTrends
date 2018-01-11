import React, { Component } from 'react';
import Button from "antd/es/button/button";
import ArtistsCascader from "./ArtistsCascader";
import { message } from "antd";

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
        if (this.state.artist === null) {
            message.error('No artist has been chosen');
        }

        else {
            console.log(this.state.artist)
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
                            <td colSpan={3} width={250}>
                                <ArtistsCascader
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
