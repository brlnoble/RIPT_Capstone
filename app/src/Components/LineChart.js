import React from "react";
import Chart from "chart.js/auto";
import { Line } from "react-chartjs-2";

//Creates the data object required for the line chart
function GetData(chartData,avg) {
    return(
        {
            labels: Array.from(Array(chartData.length).keys()), //generates labels based on length of input array
            datasets: [
              {
                backgroundColor: "#f15a24",
                borderColor: "#f15a24",
                data: chartData, //adds the data to the graph
              },

              {
                borderColor: "#999",
                data: Array.from(Array(chartData.length)).fill(avg), //average value
              }
            ],
          }
    )
};

//Styles the plot
const options = {
    plugins: {
        legend: {
            display: false
        },

        tooltip: { displayColors: false, //Hides the colour block
            callbacks: { title: function(tooltipItems, data) {return ''; }} //Hides the X-label we aren't using 
        }
    },

    scales: { x: { ticks: { display: false } } },

    maintainAspectRatio: false,

    
}

class LineChart extends React.Component {
    render() {
        const myData = GetData(this.props.chartData,this.props.avg); //Creatse the data object based on the props

        return (
            <div style={{width: "70%",height: "50%"}}>
                <Line data={myData} options={options}/>
            </div>
        );
    }
};

export default LineChart;