import React from 'react'
import MenuList from './components/MenuList.js'
import UsersList from './components/UsersList.js'
import Footer from './components/Footer.js'
import axios from 'axios'

class App extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/user/')
        .then(response => {
            const users = response.data
            this.setState({
                'users': users
            })
        })
        .catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <MenuList />
                <div>
                    <UsersList users={this.state.users} />
                </div>
                <Footer />
            </div>
        )
    }
}

export default App;
