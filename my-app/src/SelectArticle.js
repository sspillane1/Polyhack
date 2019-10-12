import React from 'react';

class SelectIssue extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            address: this.props.address,
            issue: this.props.issue,
            titles: this.props.titles,
            bodies: this.props.bodies
        };

    }
    
    makeButton(data) {
        return (
            <button
                //style={someStyle}
                onClick={() => console.log(1)}>
                {data}
            </button>
        );
    }

    render() {
        //Render the list of buttons to be selected for keywords
        return (
            <div>
                <p>
                    We found some issues currently impacting {this.state.address}
                </p>
                {this.state.issues.map((value,index)=>this.makeButton(value))}


            </div>

        )
    }

}

export default SelectIssue;