import next from 'next';
import React from 'react'

interface User {
    id: number;
    name: string;
    email: string;
    phone: string;
}
const UsersPage = async () => {

    const res = await fetch('https://jsonplaceholder.typicode.com/users',
       {cache:'no-store'}, // This ensures that the data is always fetched fresh 
    //    {next: { revalidate: 10 }} // This is for Next.js 13.4+ to revalidate the page every 10 seconds, 
    )

    const users: User[] = await res.json()
    return (
        <>
            <h1>Users</h1>
            <p>{new Date().toLocaleTimeString()}</p>
            <ul>
                {users.map((user: User) => (
                    <li key={user.id}>
                        <h2>{user.name}</h2>
                        <p>{user.email}</p>
                        <p>{user.phone}</p>
                    </li>
                ))}
            </ul>
        </>
    )
}

export default UsersPage