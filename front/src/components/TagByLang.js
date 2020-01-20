import React, {Component} from 'react';
import './TagByLang.css'

export default class TagByLang extends Component {

    constructor(props) {

        super(props)

        this.state = {
            data: []
        }

    }

    componentDidMount() {

        let url = 'http://localhost:5000/api/group-lang'

        fetch(url)
            .then(res => res.json())
            .then(json => {
                this.setState({
                    data: json
                })
            })

    }

    render() {

        return (
            <div className="tagbyname">
                <h2>Quantidade de postagens por idioma/país</h2>

               <table className="table">
                   <thead>
                   <tr>
                       <th>Nome</th>
                       <th>Followers</th>
                   </tr>
                   </thead>
                   <tbody>
                   </tbody>
               </table>
            </div>
        )
    }
}
