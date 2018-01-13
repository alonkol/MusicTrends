import React, { Component } from 'react';
import { Card } from 'antd';
import Row from "antd/es/grid/row";
import Col from "antd/es/grid/col";
import Icon from "antd/es/icon/index";
const { Meta } = Card;

class About extends Component {

    render() {
        return (
            <div>
                <Row>
                    <Col span={5} />
                    <Col span={7}>
                        <Card
                            hoverable
                            style={{ width: 240 }}
                            cover={<img alt='Oz Anani' src={require("./images/Anani.jpg")} />}
                        >
                            <Meta
                                title="Oz Anani"
                                description={<div><Icon type='github' />    @OzAn94</div>}
                            />
                        </Card>
                    </Col>
                    <Col span={7}>
                        <Card
                            hoverable
                            style={{ width: 240 }}
                            cover={<img alt='Noam Mansur' src={require("./images/Mansur.jpg")} />}
                        >
                            <Meta
                                title="Noam Mansur"
                                description={<div><Icon type='github' />    @noammansur</div>}
                            />
                        </Card>
                    </Col>
                    <Col span={5} />
                </Row>
                <br /><br />
                <Row>
                    <Col span={5} />
                    <Col span={7}>
                        <Card
                            hoverable
                            style={{ width: 240 }}
                            cover={<img alt='Yossi Elman' src={require("./images/Elman.png")} />}
                        >
                            <Meta
                                title="Yossi Elman"
                                description={<div><Icon type='github' />    @elmyossi</div>}
                            />
                        </Card>
                    </Col>
                    <Col span={7}>
                        <Card
                            hoverable
                            style={{ width: 240 }}
                            cover={<img alt='Alon Kollmann' src={require("./images/Kollmann.jpg")} />}
                        >
                            <Meta
                                title="Alon Kollmann"
                                description={<div><Icon type='github' />    @alonkol</div>}
                            />
                        </Card>
                    </Col>
                    <Col span={5} />
                </Row>
            </div>
        );
    }
}

export default About;