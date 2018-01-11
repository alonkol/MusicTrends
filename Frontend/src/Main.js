import React, { Component } from 'react';
import './App.css';
import topSongs from './api/data.json';
import TrendsChart from "./TrendsChart";
import FilterSection from "./FilterSection";
import { Layout, Menu, Icon } from 'antd';
import SubMenu from "antd/es/menu/SubMenu";
import Blacklist from "./Blacklist";
import AddSong from "./AddSong";
import UpdateSongData from "./UpdateSongData";

const { Header, Content, Footer, Sider } = Layout;

class Main extends Component {

    constructor() {
        super();
        this.state = {current_page: 'trends'}
    }

    handleClick = (e) => {
        console.log('click ', e);
        this.setState({
            current_page: e.key,
        });
    }

    render() {
        return (
            <Layout>
                <Sider
                    breakpoint="lg"
                    collapsedWidth="0"
                    onCollapse={(collapsed, type) => { console.log(collapsed, type); }}
                >
                    <div className="logo" />
                    <Menu theme="dark" mode="inline" defaultSelectedKeys={['trends']} onClick={this.handleClick}>
                        <Menu.Item key="trends">
                            <Icon type="area-chart" />
                            <span className="nav-text">Trends</span>
                        </Menu.Item>
                        <SubMenu key="manage" title={<span><Icon type="database" /><span className="nav-text">Manage</span></span>}>
                            <Menu.Item key="add-song">
                                <Icon type="user" />
                                <span className="nav-text">
                                    Add Song
                                </span>
                            </Menu.Item>
                            <Menu.Item key="update-song"><Icon type="edit" />
                                <span className="nav-text">
                                    Update Song
                                </span>
                            </Menu.Item>
                            <Menu.Item key="blacklist-artist"><Icon type="delete" />
                                <span className="nav-text">
                                    Blacklist Artist
                                </span>
                            </Menu.Item>
                        </SubMenu>
                        <Menu.Item key="about">
                            <Icon type="user" />
                            <span className="nav-text">About Us</span>
                        </Menu.Item>
                    </Menu>
                </Sider>
                <Layout>
                    <Header style={{ background: '#fff', padding: 0,  }}>
                        <h1>Music<b>Trends</b> <Icon type="sound" style={{ color: '#08c' }} /></h1>
                    </Header>
                    <Content style={{ margin: '24px 16px 0' }}>
                        <div align="center" style={{ padding: 24, background: '#fff', minHeight: '100vh'}}>
                            {this.getContent()}
                        </div>
                    </Content>
                    <Footer style={{ textAlign: 'center' }}>
                        Music Trends ©2018 Created by KMEA
                    </Footer>
                </Layout>
            </Layout>
        );
    }

    getContent() {
        if (this.state.current_page === 'trends') {
            return (
                <div>
                    <FilterSection/>
                    <br/>
                    <br/>
                    <TrendsChart topSongs={topSongs} numOfResults={5}></TrendsChart>
                </div>
            );
        }

        if (this.state.current_page === 'about') {
            return (
                <div>
                    About us
                </div>
            );
        }

        if (this.state.current_page === 'blacklist-artist') {
            return (
                <Blacklist/>
            );
        }

        if (this.state.current_page === 'add-song') {
            return (
                <AddSong/>
            );
        }

        if (this.state.current_page === 'update-song') {
            return (
                <UpdateSongData/>
            );
        }

    }

}

export default Main;
