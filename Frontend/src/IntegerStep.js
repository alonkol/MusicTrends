import React, { Component } from 'react';
import { Slider, InputNumber, Row, Col } from 'antd';

class IntegerStep extends Component {

    constructor(props) {
        super(props);

        this.state = {
            inputValue: 5
        }
    }

    onChange = (value) => {
        this.setState({
            inputValue: value,
        });

        this.props.onChange(value);
    }
    render() {
        return (
            <Row>
                <Col span={12}>
                    <Slider min={5} max={20} onChange={this.onChange} value={this.state.inputValue} />
                </Col>
                <Col span={4}>
                    <InputNumber
                        min={5}
                        max={20}
                        style={{ marginLeft: 16 }}
                        value={this.state.inputValue}
                        onChange={this.onChange}
                    />
                </Col>
            </Row>
        );
    }
}

export default IntegerStep ;