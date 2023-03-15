const pool = require('.././database/database');
const queries = require('./queries');

const getMetrics = (req, res) => { 
    pool.query(queries.getMetrics, (error, results) => {
        if (error) {
            throw error; 
        }
        res.status(200).json(results.rows);
    });
};

const getMetricsByUser = (req, res) => {
    const username = req.params.username;
    pool.query(queries.getMetricsByUser, [username], (error, results) => {
        if (error) {
            throw error;
        }
        res.status(200).json(results.rows);
    });
};

const addUser = (req, res) => {
    //using JS destructuring to get the values from the request body
    const { username, forces, accuracy, reaction, form, stability } = req.body;

    // check if user exists
    pool.query(queries.getMetricsByUser, [username], (error, results) => {
        if (error) {
            throw error;
        }
        if (results.rows.length > 0) {
            res.status(400).json({ message: "User already exists" });
        }
        else{
            pool.query(queries.addUser, [username, forces, accuracy, reaction, form, stability], (error, results) => {
                if (error) {
                    throw error;
                }
                res.status(201).json({ message: "User added successfully" });
            });
        }
    });
};

const deleteUser = (req, res) => {
    const username = req.params.username;

    pool.query(queries.getMetricsByUser, [username], (error, results) => {
        const user_does_not_exist = !results.rows.length;
        if (user_does_not_exist) {
            res.status(400).json({ message: "User does not exist" });
        }
        else {
            pool.query(queries.deleteUser, [username], (error, results) => {
                if (error) {
                    throw error;
                }
                res.status(200).json({ message: "User deleted successfully" });
            });
        }
    });
};

const updateUser = (req, res) => {
    const username = req.params.username;
    const { forces, accuracy, reaction, form, stability } = req.body;
    pool.query(queries.getMetricsByUser, [username], (error, results) => {
        const user_does_not_exist = !results.rows.length;
        if (user_does_not_exist) {
            res.status(400).json({ message: "User does not exist" });
        }
        else {
            pool.query(queries.updateUser, [forces, accuracy, reaction, form, stability, username], (error, results) => {
                if (error) {
                    throw error;
                }
                res.status(200).json({ message: "User updated successfully" });
            });
        }
    });
};


module.exports = {
    getMetrics,
    getMetricsByUser,
    addUser,
    deleteUser,
    updateUser,

};