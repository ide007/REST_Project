import React from 'react'
import {BrowserRouter, Routes , Route, Navigate, Link} from 'react-router-dom'
//import MenuList from './components/MenuList.js'
import UsersList from './components/UsersList.js'
import TaskBoard from './components/TaskBoard.js'
import ProjectList from './components/ProjectsList.js'
import ProjectInfo from './components/ProjectInfo.js'
import Footer from './components/Footer.js'
import axios from 'axios'

const NotFound404 = () => {
    return (
        <div>
            <h1>Страница не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'users': [],
            'tasks': [],
            'projects': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
        .then(response => {
            const users = response.data.results
            this.setState({
                'users': users
            })
        })
        .catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/taskboard/')
        .then(response => {
            const tasks = response.data.results
            this.setState({
                'tasks': tasks
            })
        })
        .catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project/')
        .then(response => {
            const projects = response.data.results
            this.setState({
                'projects': projects
            })
        })
        .catch(error => console.log(error))
    }

    render () {
        return (
            <div>
               <div>
                    <BrowserRouter>
                        <nav>
                        <ul>
                            <li><Link to="/">Проекты</Link> </li>
                            <li><Link to="/taskboard">Задачи</Link> </li>
                            <li><Link to="/users">Участники</Link> </li>
                            <li>
                                <form>
                                    <input type="string" />
                                    <button> Поиск </button>
                                </form>
                            </li>
                        </ul>
                        </nav>
                        <Routes>
                            <Route exact path='/' element={<ProjectList projects={this.state.projects} />} />
                            <Route exact path='/users' element={<UsersList users={this.state.users} />} />
                            <Route exact path='/taskboard' element={<TaskBoard tasks={this.state.tasks} />} />
                            <Route path='/project' element={<Navigate to='/'/>} />
                            <Route path='/project/:project_id' element={<ProjectInfo tasks={this.state.tasks} /> } />
                            <Route path='*' element={<NotFound404 /> } />
                        </Routes>
                    </BrowserRouter>
                </div>
                <Footer />
            </div>
        )
    }
}

export default App;
