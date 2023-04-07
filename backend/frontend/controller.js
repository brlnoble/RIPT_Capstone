const pool = require('.././database/database');
const queries_users = require('.././users/queries');
const queries_metrics = require('.././metrics/queries');
const queries_sessions = require('.././sessions/queries');

const getEverything = async (req, res) => {

    // Do our queries
    const username = req.params.username;
    user_query = await pool.query(queries_users.getUsersByUsername, [username]);
    metrics_query = await pool.query(queries_metrics.getMetricsByUser, [username]);
    sessions_query = await pool.query(queries_sessions.get10SessionsByUser, [username]);

    // Save JSON responses
    user = user_query.rows[0];
    metrics = metrics_query.rows[0];
    sessions = sessions_query.rows;

    //Create the Mega JSON
    const mega_json = {"Profile": user, "averageMetrics": metrics, "sessions": sessions};
    res.status(200).json(mega_json);

};


module.exports = {
    getEverything,

}

