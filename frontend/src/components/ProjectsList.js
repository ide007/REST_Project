import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.project_id}</td><br />
            <td><Link to={`/project/${project.project_id}`} > {project.name}</Link></td><br />
            <td>{project.project_user}</td><br />
            <td>{project.repository_link}</td><br />
        </tr>
    )
}

const ProjectsList = ({projects}) => {
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
            {projects.map((project) => <ProjectItem project={project}/> )}
        </table>
    )
}

export default ProjectsList;
