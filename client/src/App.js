import React,{Component} from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from './login.jsx';
import './App.css';
// import { PrivateRoute } from "./PrivateRoute.jsx";
// import {isLoggedIn} from './auth.js';

const Home = ()=> <div className="content">
                    <div className="person_info">
                      {/*<p>Профиль: {localStorage.getItem("fio")}</p>*/}
                      <p>Баланс: 200 р.</p>
                      <p>Дата оплаты: 31.12.2020</p>
                      <p>Сумма к оплате: 300 р.</p>
                      <button className="btn btn-danger btn-pay">
                        Пополнить
                      </button>
                    </div>
                    <div className="card_info hidden">
                      <div className="input-group mb-3">
                        <div className="input-group-prepend">
                          <span className="input-group-text" id="basic-addon1">@</span>
                        </div>
                        <input type="text" className="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1"/>
                      </div>
                    </div>
                </div>

export default class App extends Component{
  constructor(props){
    super(props);

    this.state = {
      access_token:"",
      fio:""
    }
  }

  render(){
    return(
      <Router>
        <div>
          <Route exact path="/" component={Home} />
          <Route exact path="/login" component={Login} />
          {/*}PrivateRoute exact isloggedin={isLoggedIn()} path="/" component={Home} />
          <Route exact path="/login" component={Login} /> */}
        </div>
    </Router>
      )
  }
}