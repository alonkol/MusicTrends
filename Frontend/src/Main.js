import React, { Component } from 'react';
import './App.css';
import topSongs from './api/data.json';
import TrendsChart from "./TrendsChart";
import FilterSection from "./FilterSection";
import { Layout, Menu, Icon } from 'antd';
import Management from "./Management";

const { Header, Content, Footer, Sider } = Layout;

class Main extends Component {

    constructor() {
        super();
        this.state = {current_page: 'manage'}
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
                        <Menu.Item key="manage">
                            <Icon type="database" />
                            <span className="nav-text">Manage</span>
                        </Menu.Item>
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

        if (this.state.current_page === 'manage') {
            return (
                <Management/>
            );
        }

        if (this.state.current_page === 'about') {
            return (
                <div>
                    About us
                </div>
            );
        }
    }

}

export default Main;
