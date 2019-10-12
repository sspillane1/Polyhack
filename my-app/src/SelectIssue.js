import React from 'react';
import Button from 'react-bootstrap/Button';


class SelectIssue extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            address: this.props.address,
            issues: [
                "Homelessness",
                "Rent Control",
                "Immigration",
                "Construction",
                "Jobs"
            ]
        };

    }

    getSummary(){
        //send the thing you're looking for
        //wait for response from server
        //change and populate page.
    }

    makeButton(data,ind) {
        return (
            <div>
            <Button className ="issueblock" key={ind}               //style={someStyle}
                onClick={(data,key) => console.log(key)}>
                {data}
            </Button>
            <br></br>
            </div>
        );
    }

    render() {
        //Render the list of buttons to be selected for keywords
        return (
            <div>
                <h2>
                    Select topic of focus for information retrieval about {this.state.address}
                </h2>
                <ul className>
                {this.state.issues.map((value,index)=>this.makeButton(value,index))}
                </ul>


            </div>

        )
    }

}

export default SelectIssue;
