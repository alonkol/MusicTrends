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
import About from "./About";
import Search from "./Search";
import { getParam } from './Utils.js';

const { Header, Content, Footer, Sider } = Layout;

class Main extends Component {

    constructor() {
        super();
        this.state = {current_page: 'trends',
            numberOfResults: 5,
            selectedCategory: 0,
            selectedCategoryFilter: "?category=0"
        }
    }

    handleClick = (e) => {
        console.log('click ', e);
        this.setState({
            current_page: e.key,
        });
    }

    handleSliderChange = (value) => {
        this.setState({numberOfResults: value});
        console.log(value);
    }

    handleCategoryChange = (value) => {
        this.setState({selectedCategory: value});
        this.setState({selectedCategoryFilter: "?category=" + value})
    }

    render() {
        this.manageSubMenu = <SubMenu key="manage" title={<span><Icon type="database" /><span className="nav-text">Manage</span></span>}>
                            <Menu.Item key="add-song">
                                <Icon type="plus-circle-o" />
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

        const key = getParam("key");
        if (!(key && key !== undefined && key !== "")){
            this.manageSubMenu = "";
        }

        return (
            <Layout>
                <Sider
                    breakpoint="lg"
                    collapsedWidth="0"
                    handleSliderChange={this.handleSliderChange}
                    onCollapse={(collapsed, type) => { console.log(collapsed, type); }}
                >
                    <div className="logo" />
                    <Menu theme="dark" mode="inline" defaultSelectedKeys={['trends']} onClick={this.handleClick}>
                        <Menu.Item key="trends">
                            <Icon type="area-chart" />
                            <span className="nav-text">Trends</span>
                        </Menu.Item>
                        {this.manageSubMenu}
                        <Menu.Item key="search">
                            <Icon type="search" />
                            <span className="nav-text">Find Song</span>
                        </Menu.Item>
                        <Menu.Item key="about">
                            <Icon type="user" />
                            <span className="nav-text">The Team</span>
                        </Menu.Item>
                    </Menu>
                </Sider>
                <Layout>
                    <Header style={{ padding: 0, margin:20 }}>
                        <h1>music<b>trends</b> <Icon type="sound" style={{ color: '#08c' }} /></h1>
                    </Header>
                    <Content style={{ margin: '24px 16px 0' }}>
                        <div align="center" style={{ padding: 24, background: '#fff', minHeight: '100vh', overflow: 'hidden'}}>
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
                    <FilterSection
                        handleCategoryChange={this.handleCategoryChange}
                        handleSliderChange={this.handleSliderChange}
                    />
                    <br/>
                    <br/>
                    <TrendsChart topSongs={topSongs} numberOfResults={this.state.numberOfResults} selectedCategoryFilter={this.state.selectedCategoryFilter}></TrendsChart>
                </div>
            );
        }

        if (this.state.current_page === 'about') {
            return (
                <About />
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

        if (this.state.current_page === 'search') {
            return (
                <Search/>
            );
        }

    }

}

export default Main;
