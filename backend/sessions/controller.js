const pool = require('.././database/database');
const queries = require('./queries');


const getSessions = (req, res) => { 
    pool.query(queries.getSessions, (error, results) => {
        if (error) {
            throw error; 
        }
        res.status(200).json(results.rows);
    });
};

const getSessionsByUsername = (req, res) => {
    const username = req.params.username;
    pool.query(queries.getSessionsByUsername, [username], (error, results) => {
        if (error) {
            throw error;
        }
        res.status(200).json(results.rows);
    });
};

const addSession = (req, res) => {
    const { session_id, username, category, datetime, duration, metrics } = req.body;
    pool.query(queries.addSession, [session_id, username, category, datetime, duration, metrics], (error, results) => {
        if (error) {
            throw error;
        }
        res.status(201).send(`Session added with ID: ${session_id}}`);
    });
};

const get10SessionsByUser = (req, res) => {
    const username = req.params.username;
    pool.query(queries.get10SessionsByUser, [username], (error, results) => {
        if (error) {
            throw error;
        }
        //console.log(results.rows.length);
        res.status(200).json(results.rows);
    });
};


module.exports = {
    getSessions,
    getSessionsByUsername,
    addSession,
    get10SessionsByUser,

};