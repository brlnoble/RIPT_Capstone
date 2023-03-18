// SQL queries for users go in here

const getUsers = 'SELECT * FROM users';
const getUsersbyUsername = 'SELECT * FROM users WHERE username = $1';
const addUser = 'INSERT INTO users (username, first_name, email, birthday, membership, session_num, isorthodox, picture) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)';

module.exports = {
    getUsers,
    getUsersbyUsername,
    addUser,
}