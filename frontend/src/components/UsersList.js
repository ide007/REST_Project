const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.id}</td><br />
            <td>{user.user_name}</td><br />
            <td>{user.first_name}</td><br />
            <td>{user.last_name}</td><br />
            <td>{user.email}</td><br />
        </tr>
    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>
                ID
            </th><br />
            <th>
                Ник (логин)
            </th><br />
            <th>
                Имя
            </th><br />
            <th>
                Фамилия
            </th><br />
            <th>
                Email
            </th><br />
            {users.map((user) => <UserItem user={user}/> )}
        </table>
    )
}

export default UsersList;
