
const TaskItem = ({task}) => {
    return (
        <tr>
            <td>{task.id}</td><br />
            <td>{task.task_title}</td><br />
            <td>{task.task_status}</td><br />
            <td>{task.project}</td><br />
            <td>{task.creator}</td><br />
            <td>{task.task_description}</td><br />
            <td>{task.created_time}</td><br />
        </tr>
    )
}

const TaskBoard = ({tasks}) => {
    return (
        <table>
            <th>
                Id
            </th><br />
            <th>
                Название
            </th><br />
            <th>
                Статус
            </th><br />
            <th>
                Проект
            </th><br />
            <th>
                Пользователь
            </th><br />
            <th>
                Текст Задачи
            </th><br />
            <th>
                Дата создания
            </th><br />
            {tasks.map((task) => <TaskItem task={task}/> )}
        </table>
    )
}

export default TaskBoard;
