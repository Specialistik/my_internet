import React, { Component } from "react";

export default class Landing extends Component{
    constructor(props){
        super(props);
        this.state = {
            token:localStorage.getItem('token'),
        }
    }

   render(){
        return (
            <div>
                
            </div>
        )
    }
}