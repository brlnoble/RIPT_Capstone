const { Router } = require('express');
const controller = require('./controller');

const router = Router();

router.get('/:username', controller.getEverything);

module.exports = router;