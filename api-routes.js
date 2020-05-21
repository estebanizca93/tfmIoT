// api-routes.js
// Initialize express router
let router = require('express').Router();

// Set default API response
router.get('/', function (req, res) {
    res.json({
        status: 'API Its Working',
        message: 'Welcome to RESTHub crafted with love!',
    });
});
// Import sigfox controller
var sigfoxController = require('./sigfoxController');
// Sigfox routes
router.route('/sigfox')
    .get(sigfoxController.index)
    .post(sigfoxController.new);
// API TIME
router.route('/timemilis')
    .get(function (req, res) {
        res.json({
            time: Date.now()
        });
    });
// Export API routes
module.exports = router;