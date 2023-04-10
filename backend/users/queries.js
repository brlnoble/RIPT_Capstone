// SQL queries for users go in here

const getUsers = 'SELECT username, first_name, email, TO_CHAR(birthday, \'YYYY/MM/DD HH:MM:SS\') AS "birthday" ,TO_CHAR(membership, \'YYYY/MM/DD HH:MM:SS\') AS "membership", session_num, isorthodox, picture FROM users';
const getUsersByUsername = 'SELECT username, first_name, email, TO_CHAR(birthday, \'YYYY/MM/DD HH:MM:SS\') AS "birthday" ,TO_CHAR(membership AS "membership", \'YYYY/MM/DD HH:MM:SS\'), session_num, isorthodox, picture FROM users WHERE username = $1';
const addUser = 'INSERT INTO users (username, first_name, email, birthday, membership, session_num, isorthodox, picture) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)';
const deleteUser = 'DELETE FROM users WHERE username = $1';
const updateUser = 'UPDATE users SET first_name = $1, email = $2, birthday = $3, membership = $4, session_num = $5, isorthodox = $6, picture = $7 WHERE username = $8'

module.exports = {
    getUsers,
    getUsersByUsername,
    addUser,
    deleteUser,
    updateUser,

}