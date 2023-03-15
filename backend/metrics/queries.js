//SQL queries go in here

const getMetrics = 'SELECT * FROM metrics';
const getMetricsByUser = 'SELECT * FROM metrics WHERE username = $1';
const addUser = 'INSERT INTO metrics (username, forces, accuracy, reaction, form, stability) VALUES ($1, $2, $3, $4, $5, $6)';
const deleteUser = 'DELETE FROM metrics WHERE username = $1';
const updateUser = 'UPDATE metrics SET forces = $1, accuracy = $2, reaction = $3, form = $4, stability = $5 WHERE username = $6'

module.exports = {
    getMetrics,
    getMetricsByUser,
    addUser,
    deleteUser,
    updateUser
}