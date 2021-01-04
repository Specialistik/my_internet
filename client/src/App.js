import React, {Component} from 'react';
//import Login from "./login";
import Cabinet from "./cabinet";
import './App.css';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      token: localStorage.getItem('access-token') || null,
    }
  }
  render = () => {
    /*if (this.state.token === null) {
      return <Login />
    } else { */
      return <Cabinet />
    //}
    //return (this.state.token === null) ? <Login /> : <Cabinet />
  }
}