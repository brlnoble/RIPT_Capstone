// SQL queries for sessions go in here

const getSessions = 'SELECT * FROM sessions';
const getSessionsByUsername = 'SELECT * FROM sessions WHERE username = $1';
const addSession = 'INSERT INTO sessions (session_id, username, category, datetime, duration, metrics) VALUES ($1, $2, $3, $4, $5, $6)';
const get10SessionsByUser = 'SELECT * FROM sessions WHERE username = $1 ORDER BY datetime DESC LIMIT 10';


module.exports = {
    getSessions,
    getSessionsByUsername,
    addSession,
    get10SessionsByUser,
}