
const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.user_name}</td><br />
            <td>{user.first_name}</td><br />
            <td>{user.last_name}</td><br />
            <td>{user.email}</td>
        </tr>
    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>
                Ник (логин)
            </th><br />
            <th>
                Имя пользователя
            </th><br />
            <th>
                Фамилия
            </th><br />
            <th>
                Почта
            </th>
            {users.map((user) => <UserItem user={user}/> )}
        </table>
    )
}

export default UsersList;