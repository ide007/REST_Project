import React from 'react'
import {BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'
//import MenuList from './components/MenuList.js'
import UsersList from './components/UsersList.js'
import TaskBoard from './components/TaskBoard.js'
import ProjectList from './components/ProjectsList.js'
import ProjectInfo from './components/ProjectInfo.js'
import LoginForm from './components/LoginForm.js'
import ProjectForm from './components/ProjectForm.js'
import Footer from './components/Footer.js'
import axios from 'axios'


const NotFound = () => {
    let location = useLocation()
    return (
        <div>Page {location.pathname} not found</div>
    )
}


class App extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'users': [],
            'tasks': [],
            'projects': [],
            'token': ''
        }
    }

    get_token(login, password) {
        axios
        .post('http://127.0.0.1:8000/api-token-auth/', {'username': login, 'password': password})
        .then(response => {
            const token = response.data.token
            localStorage.setItem('token', token)
            this.setState({
                'token': token
            }, this.get_data)
        })
        .catch(error => console.log(error))
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({
                'token': ''
            }, this.get_data)
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
                'token': token
            }, this.get_data)
    }

    is_auth() {
        return !!this.state.token
    }

    get_headers() {
        if (this.is_auth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    get_data() {
        let headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
        .then(response => {
            const users = response.data
            this.setState({
                'users': users
            })
        })
        .catch(error => {
            this.setState({
                'users': []
            })
            console.log(error)
        })

        axios.get('http://127.0.0.1:8000/api/taskboard/', {headers})
        .then(response => {
            const tasks = response.data
            this.setState({
                'tasks': tasks
            })
        })
        .catch(error => {
            this.setState({
                'tasks': []
            })
            console.log(error)
        })

        axios.get('http://127.0.0.1:8000/api/project/', {headers})
        .then(response => {
            const projects = response.data
            this.setState({
                'projects': projects
            })
        })
        .catch(error => {
            this.setState({
                'projects': []
            })
            console.log(error)
        })
    }

    delete_project (id) {
        let headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers})
        .then(response => {
            const projects = response.data
            this.setState({
                'projects': this.state.projects.filter((project) => project.project_id !== id)
            })
        })
        .catch(error => {
            console.log(error)
        })
    }

    create_project(name, repository_link, users) {
        let headers = this.get_headers()
        axios.post('http://127.0.0.1:8000/api/project/', {
         'name': name,
         'repository_link': repository_link,
         'project_user': users
         }, {headers})
        .then(response => {
            this.get_data();
        })
        .catch(error => {
            console.log(error)
        })
        console.log(name, repository_link, users)
    }

    render () {
        return (
            <div>
               <div>
                    <BrowserRouter>
                        <nav>
                        <ul>
                            <li><Link to='/'>Проекты</Link> </li>
                            <li><Link to='/create'>Создать проект</Link> </li>
                            <li><Link to='/taskboard'>Задачи</Link> </li>
                            <li><Link to='/users'>Участники</Link> </li>
                            <li>
                                {this.is_auth() ?
                                <button onClick={() => this.logout()}>Выйти</button>:
                                 <Link to='/login'>Войти</Link> }
                            </li>
                            <li>
                                <form>
                                    <input type='string' />
                                    <button> Поиск проекта </button>
                                </form>
                            </li>
                        </ul>
                        </nav>
                        <Routes>
                            <Route exact path='/' element={<ProjectList projects={this.state.projects}
                             delete_project={(id) => this.delete_project(id)} />} />
                            <Route exact path='/create' element={<ProjectForm users={this.state.users}
                             create_project={(name, repository_link, users) => this.create_project(name, repository_link, users)} />} />
                            <Route exact path='/users' element={<UsersList users={this.state.users} />} />
                            <Route exact path='/login' element={<LoginForm
                             get_token={(login, password) => this.get_token(login, password)}/>} />
                            <Route exact path='/taskboard' element={<TaskBoard
                             tasks={this.state.tasks} />} />
                            <Route path='/project' element={<Navigate to='/'/>} />
                            <Route path='/project/:project_id' element={<ProjectInfo
                             tasks={this.state.tasks} /> } />
                            <Route path="*" element={<NotFound /> } />
                        </Routes>
                    </BrowserRouter>
                </div>
                <Footer />
            </div>
        )
    }
}

export default App;
