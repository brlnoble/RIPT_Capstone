// SQL queries for sessions go in here

const getSessions = 'SELECT session_id, username, to_char(datetime, \'YYYY/MM/DD HH:MM:SS/\') AS "datetime", to_char(duration, \'HH24:MI:SS\') AS "duration", metrics FROM sessions';
const getSessionsByUsername = 'SELECT session_id, username, to_char(datetime, \'YYYY/MM/DD HH:MM:SS/\') AS "datetime", to_char(duration, \'HH24:MI:SS\') AS "duration", metrics FROM sessions WHERE username = $1';
const addSession = 'INSERT INTO sessions (session_id, username, category, datetime, duration, metrics) VALUES ($1, $2, $3, $4, $5, $6)';
const get10SessionsByUser = 'SELECT session_id, username, to_char(datetime, \'YYYY/MM/DD HH:MM:SS/\') AS "datetime", to_char(duration, \'HH24:MI:SS\') AS "duration", metrics FROM sessions	WHERE username = $1 ORDER BY datetime DESC LIMIT 10';


module.exports = {
    getSessions,
    getSessionsByUsername,
    addSession,
    get10SessionsByUser,
}