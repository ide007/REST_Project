import {Link} from 'react-router-dom'

const ProjectItem = ({project, delete_project}) => {
    return (
        <tr>
            <td>{project.project_id}</td><br />
            <td><Link to={`/project/${project.project_id}`} > {project.name} </Link></td><br />
            <td>{project.project_user}</td><br />
            <td>{project.repository_link}</td><br />
            <td><button onClick={()=>delete_project(project.project_id)}  type='button'>Удалить</button></td><br />
        </tr>
    )
}

const ProjectsList = ({projects, delete_project}) => {
    return (
        <table>
            <th>
                ID
            </th><br />
            <th>
                Название проекта
            </th><br />
            <th>
                Участники
            </th><br />
            <th>
                ссылка на проект
            </th><br />
            {projects.map((project) => <ProjectItem project={project} delete_project={delete_project}/> )}
        </table>
    )
}

export default ProjectsList;
