import React, {Component} from 'react';
import './TweetsHour.css'
import { Chart } from "react-google-charts";

export default class TweetsHour extends Component {

    constructor(props) {

        super(props)

        this.state = {
            data: []
        }

    }

    componentDidMount() {

        let url = 'http://10.0.0.103:5000/api/group-hrs'

        fetch(url)
            .then(res => res.json())
            .then(json => {
                this.setState({
                    data: json
                })
            })

    }

    render() {

        let data = []

        data.push(["Horário", "Quantidade", { role: 'annotation' }])

        for(let item of this.state.data) {

            data.push([item.hours + 'h', item.tweets, item.tweets])

        }

        var options = {
            title: 'Quantidade de tweets por hora do dia',
            bar: {groupWidth: "30%"},
            height: 300
        };

        return (
            <div className="tweetshour">
                <h2>Total de postagens agrupadas por hora do dia</h2>
                <Chart
                    chartType="ColumnChart"
                    width="100%"
                    height="400px"
                    data={data}
                    options={options}
                    />
            </div>
        )
    }

}
