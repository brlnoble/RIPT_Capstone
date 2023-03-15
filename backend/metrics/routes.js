const { Router } = require('express');
const controller = require('./controller');

const router = Router();

router.get('/', controller.getMetrics);
router.post('/', controller.addUser);
router.get('/:username', controller.getMetricsByUser);
router.delete('/:username', controller.deleteUser);
router.put('/:username', controller.updateUser);

module.exports = router;
