const { Router } = require('express');
const controller = require('./controller');

const router = Router();    

router.get('/', controller.getSessions);
router.post('/', controller.addSession);
router.get('/:username', controller.getSessionsByUsername);
router.get('/last_10/:username', controller.get10SessionsByUser);

module.exports = router;