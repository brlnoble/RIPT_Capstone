import React from "react"

class FilterForm extends React.Component {
    render() {
        return(
            <>
                <h2>Filter Results</h2>
                <form className="session_search">

                    <div className="filter_category">
                        <h3>Category</h3>
                        <div className="filter_input">
                            <input type="checkbox" id="category_personalized" checked={true}></input>
                            <label for="category_personalized">Personalized</label>
                        </div>
                        <div className="filter_input">
                            <input type="checkbox" id="category_endurance" checked={true}></input>
                            <label for="category_endurance">Endurance</label>
                        </div>
                        <div className="filter_input">
                            <input type="checkbox" id="category_speed" checked={true}></input>
                            <label for="category_speed">Speed</label>
                        </div>
                    </div>
                    <div className="filter_category">
                        <h3>Date</h3>
                        <div className="filter_input">
                            <input type="radio" id="date_all" name="date_select" checked></input>
                            <label for="date_all">All Sessions</label>
                        </div>
                        <div className="filter_input">
                            <input type="radio" id="date_month" name="date_select"></input>
                            <label for="date_month">This Month</label>
                        </div>
                        <div className="filter_input">
                            <input type="radio" id="date_week" name="date_select"></input>
                            <label for="date_week">This Week</label>
                        </div>
                    </div>
                    <button type="submit">Filter</button>
                </form>
            </>
        )
    }
}

export default FilterForm