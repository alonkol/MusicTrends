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
import Input from "antd/es/input/Input";

const { Header, Content, Footer, Sider } = Layout;

class Main extends Component {

    constructor() {
        super();
        this.state = {current_page: 'trends',
            numberOfResults: 5,
            selectedCategory: null,
            selectedCategoryFilter: "",
            filterSwitchOn: false
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

        if (this.state.filterSwitchOn) {
            if (value != null) {
                this.setState({selectedCategoryFilter: "?category=" + value})
            }
        }

        else {
            this.setState({selectedCategoryFilter: ""});
        }
    }

    handleSwitchChange = (value) => {
        this.setState({filterSwitchOn: value});

        if (value) {
            if (this.state.selectedCategory != null) {
                this.setState({selectedCategoryFilter: "?category=" + this.state.selectedCategory})
            }
        }

        else {
            this.setState({selectedCategoryFilter: ""});
        }
    }

    render() {
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
                        <SubMenu key="manage" title={<span><Icon type="database" /><span className="nav-text">Manage</span></span>}>
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
                            <Menu.Item key="secretKey" disabled={true}>
                                <Input  id={'secretKey'} placeholder={"Secret Key"} type='password' />
                            </Menu.Item>
                        </SubMenu>
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
                    <Header style={{ background: '#fff', padding: 0,  }}>
                        <h1>music<b>trends</b> <Icon type="sound" style={{ color: '#08c' }} /></h1>
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
                    <FilterSection
                        handleCategoryChange={this.handleCategoryChange}
                        handleSliderChange={this.handleSliderChange}
                        handleSwitchChange={this.handleSwitchChange}
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
