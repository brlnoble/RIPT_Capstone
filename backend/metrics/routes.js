const { Router } = require('express');
const controller = require('./controller');

const router = Router();

router.get('/', controller.getMetrics);
router.post('/', controller.addUserMetrics);
router.get('/:username', controller.getMetricsByUser);
router.delete('/:username', controller.deleteUserMetrics);
router.put('/:username', controller.updateUserMetrics);

module.exports = router;
