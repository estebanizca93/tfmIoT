// sigfoxModel.js
var mongoose = require('mongoose');// Setup schema
var sigfoxSchema = mongoose.Schema({
    device: String,
    data: String,
    time: String,
    duplicate: String,
    snr: String,
    dateSplitSeconds: String,
    dateSplitMiliSeconds: String,
    dataInMiliseconds: String,
    data: String,
    latencyMiliSeconds: String,
    dateParse: String,
    dataToAbsoluteTime: String,
    avgSnr: String,
    lat: String,
    lng: String,
    rssi: String,
    deviceTypeId: String,
    create_date: {
        type: String,
        default: Date.now
    },
});// Export Sigfox model
var Sigfox = module.exports = mongoose.model('initAndTicksMS', sigfoxSchema);
module.exports.get = function (callback, limit) {
    Sigfox.find(callback).limit(limit);
}