import {useParams} from 'react-router-dom'

const TaskItem = ({task}) => {
    return (
        <tr>
            <td>{task.id}</td><br />
            <td>{task.task_title}</td><br />
            <td>{task.project}</td><br />
            <td>{task.creator}</td><br />
            <td>{task.task_description}</td><br />
            <td>{task.created_time}</td><br />
        </tr>
    )
}

const ProjectInfo = ({tasks}) => {
    let {id} = useParams();
    let filteredTasks = tasks.filter((task) => task.project.includes(parseInt(id)))

    return (
        <table>
            <th>№ Задачи</th><br />
            <th>Название </th><br />
            <th>Проект</th><br />
            <th>Участники</th><br />
            <th>Описание</th><br />
            <th>Дата/Время создания</th><br />
            {filteredTasks.map((task) => <TaskItem task={task} />)}
        </table>
    )
}

export default ProjectInfo;
