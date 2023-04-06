const { Router } = require('express');
const controller = require('./controller');

const router = Router();

router.get('/', controller.getUsers);
router.post('/', controller.addUser);
router.get('/:username', controller.getUsersbyUsername);
router.delete('/:username', controller.deleteUser);
router.put('/:username', controller.updateUser);

module.exports = router;