import React, {Component} from 'react';
// import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Login from "./login";
import Cabinet from "./cabinet";
import './App.css';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      token: localStorage.getItem('access-token') || null,
    }
  }
  render(){
    return(
      (this.state.token === null) ? <Login /> : <Cabinet />
      /*<Router>
        <div>
          <Switch>
            <Route exact path="/login" component={ Login } />
            <Route exact path="" component={ Home } />
          </Switch>
        </div>
      </Router>*/
    )
  }
}