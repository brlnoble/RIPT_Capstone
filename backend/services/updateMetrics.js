const pool = require('.././database/database');
const metrics_queries = require('.././metrics/queries');
const sessions_queries = require('.././sessions/queries');


const updateMetricsValues = async (username) => {
    const sessions_query = await pool.query(sessions_queries.get10SessionsByUser,[username]);
    var sessions = sessions_query.rows;

    var forces = 0;
    var accuracy = 0;
    var reaction = 0;
    var form = 0;
    var stability = 0;

    for (i of sessions) {

        let length = sessions.length;
        let hook = i.metrics.metrics.hook;
        let uppercut = i.metrics.metrics.uppercut;
        let straight = i.metrics.metrics.straight;
        let performance = i.metrics.metrics.performance;

        forces += (hook.force.avg + uppercut.force.avg + straight.force.avg)/(3*length);
        accuracy += (hook.accuracy.avg + uppercut.accuracy.avg + straight.accuracy.avg)/(3*length);
        reaction += (hook.reaction.avg + uppercut.reaction.avg + straight.reaction.avg)/(3*length);
        //console.log(reaction);
        form += (hook.form.avg + uppercut.form.avg + straight.form.avg)/(3*length);
        stability += (performance.avg)/length;
        
    };

    new_metrics = {"username": username, "forces": forces, "accuracy": accuracy, "reaction": reaction, "form": form, "stability": stability};

    //console.log(new_metrics);

    pool.query(metrics_queries.updateUserMetrics, [forces, accuracy, reaction, form, stability, username], (error, results) => {
        if (error) {
            throw error;
        }
        console.log("Metrics updated");
    });


};


module.exports = {
    updateMetricsValues,
}
