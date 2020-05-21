// contactController.js
// Import contact model
Sigfox = require('./sigfoxModel');

var dateSplitSeconds = 0;
var dateSplitMiliSeconds = 0;
// Handle index actions
exports.index = function (req, res) {
    Sigfox.get(function (err, sigfox) {
        if (err) {
            res.json({
                status: "error",
                message: err,
            });
        }
        res.json({
            status: "success",
            message: "Sigfox data registered.",
            data: sigfox
        });
    });
};// Handle create contact actions
exports.new = function (req, res) {
    var sigfox = new Sigfox();
    Sigfox.count(function (err, count) {
        if (!err && count === 0) {
            console.log("No hay datos. Primera insercción: ", req.body.data);
        }else if(!err && count >= 1){
        }
    });
    sigfox.device = req.body.device ? req.body.device : sigfox.device;
    sigfox.time = req.body.time;
    sigfox.duplicate = req.body.duplicate;
    sigfox.snr = req.body.snr;
    sigfox.station = req.body.station;
    sigfox.dateSplitSeconds = req.body.data.toString().substring(0,10);
    sigfox.dateSplitMiliSeconds = req.body.data.toString().substring(req.body.data.toString().length -3, req.body.data.toString().length)
    sigfox.dataInMiliseconds = sigfox.dateSplitSeconds + '' +  sigfox.dateSplitMiliSeconds;
    sigfox.data = req.body.data.toString();
    sigfox.latencySeconds = parseInt(sigfox.create_date.toString().substring(0,10)) - parseInt(sigfox.dateSplitSeconds);
    sigfox.latencyMiliSeconds = parseInt(sigfox.create_date) - parseInt(sigfox.dataInMiliseconds);
    sigfox.avgSnr = req.body.avgSnr;
    sigfox.lat = req.body.lat;
    sigfox.lng = req.body.lng;
    sigfox.rssi = req.body.rssi;
    sigfox.seqNumber = req.body.seqNumber;
    sigfox.deviceTypeId = req.body.deviceTypeId;
    console.log("Objeto guardado!: ",sigfox);
    

    // save the contact and check for errors
    sigfox.save(function (err) {
        if (err) {
            res.json(err);
        } else {
            res.json({
                message: "New sigfox data created!",
                data: sigfox
            });
        }  
    });
};