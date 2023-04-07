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

const getUsersByUsername = (req, res) => {
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

const deleteUser = (req, res) => {
    const username = req.params.username;
    pool.query(queries.getUsersbyUsername, [username], (error, results) => {
        if (error) {
            throw error;
        }
        if (results.rows.length == 0) {
            res.status(400).json({ message: "User does not exist" });
        }
        else{
            pool.query(queries.deleteUser, [username], (error, results) => {
                if (error) {
                    throw error;
                }
                res.status(201).json({ message: "User deleted successfully" });
            });
        }   
    });
};

const updateUser = (req, res) => {
    const username = req.params.username;
    const { first_name, email, birthday, membership, session_num, isorthodox, picture } = req.body;
    pool.query(queries.getUsersbyUsername, [username], (error, results) => {
        if (error) {
            throw error;
        }
        if (results.rows.length == 0) {
            res.status(400).json({ message: "User does not exist" });
        }
        else{
            pool.query(queries.updateUser, [first_name, email, birthday, membership, session_num, isorthodox, picture, username], (error, results) => {
                if (error) {
                    throw error;
                }
                res.status(201).json({ message: "User updated successfully" });
            });
        }
    });
};




module.exports = {
    getUsers,
    getUsersByUsername,
    addUser,
    deleteUser,
    updateUser,
}