
const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.user_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>
                User name
            </th>
            <th>
                Last name
            </th>
            <th>
                Email
            </th>
            {users.map((user) => <UserItem user={user}/> )}
        </table>
    )
}

export default UsersList;