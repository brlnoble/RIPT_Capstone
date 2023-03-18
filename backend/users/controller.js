const pool = require('.././database/database');
const queries = require('./queries');

const getUsers = (req, res) => { 
    pool.query(queries.getUsers, (error, results) => {
        if (error) {
            throw error; 
        }
        res.status(200).json(results.rows);
    });
};

const getUsersbyUsername = (req, res) => {
    const username = req.params.username;
    pool.query(queries.getUsersbyUsername, [username], (error, results) => {
        if (error) {
            throw error;
        }
        res.status(200).json(results.rows);
    });
};

const addUser = (req, res) => {
    const { username, first_name, email, birthday, membership, session_num, isorthodox, picture } = req.body;
    
    pool.query(queries.getUsersbyUsername, [username], (error, results) => {
        if (error) {
            throw error;
        }
        if (results.rows.length > 0) {
            res.status(400).json({ message: "User already exists" });
        }
        else{
            pool.query(queries.addUser, [username, first_name, email, birthday, membership, session_num, isorthodox, picture], (error, results) => {
                if (error) {
                    throw error;
                }
                res.status(201).json({ message: "User added successfully" });
            });
        }   
    });

};

module.exports = {
    getUsers,
    getUsersbyUsername,
    addUser,

}