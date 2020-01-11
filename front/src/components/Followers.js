import React, {Component} from 'react';
import './Followers.css'

export default class Followers extends Component {

    constructor(props) {

        super(props)

        this.state = {
            data: []
        }

    }

    componentDidMount() {

        let url = 'http://10.0.0.103:5000/api/show-fls'

        fetch(url)
            .then(res => res.json())
            .then(json => {
                this.setState({
                    data: json
                })
            })

    }

    createTable() {

        let table = []

       for(let item of this.state.data) {

            let row = []
            row.push(<td>{item._id.user_name}</td>)
            row.push(<td>{item._id.followers_count}</td>)

            table.push(<tr>{row}</tr>)

       }

        return table

    }

    render() {

        return (
            <div className="followers">
                <h2>Cinco usuários da amostra com mais seguidores</h2>

               <table className="table">
                   <thead>
                   <tr>
                       <th>Nome</th>
                       <th>Followers</th>
                   </tr>
                   </thead>
                   <tbody>
                    {this.createTable()}
                   </tbody>
               </table>
            </div>
        )
    }

}