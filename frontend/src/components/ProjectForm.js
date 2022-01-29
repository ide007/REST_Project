import React from 'react'

class ProjectForm extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'name': '',
            'repository_link': '',
            'users': [],
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleUsersChoice(event) {
        if(!event.target.selectedOptions) {
            return;
        }

        let users = []
        for (let i=0; i < event.target.selectedOptions.length; i++) {
            users.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'users': users
        })
    }

    handleSubmit(event) {
        this.props.create_project(this.state.name, this.state.repository_link, this.state.users)
        event.preventDefault();
    }

    render () {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)} >
                <input type='text' name='name' placeholder='Название проекта'
                    value={this.state.name}
                    onChange={(event) => this.handleChange(event)}/>
                <input type='text' name='repository_link' placeholder='Ссылка на проект'
                    value={this.state.repository_link}
                    onChange={(event) => this.handleChange(event)}/>
                <select multiple name='users' onChange={(event)=>this.handleUsersChoice(event)}>
                 {this.props.users.map((user) => <option value={user.id}>{user.first_name} {user.last_name}</option>)}
                </select>
                <input type='submit' value='Создать' />
            </form>
        )
    }
}

export default ProjectForm
