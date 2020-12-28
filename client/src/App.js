import React, {Component} from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from "./login";
import './App.css';

class Home extends Component {
  constructor(props) {
    super(props);
    this.toggleCardInfo = this.toggleCardInfo.bind(this);
    this.pickPaymentType = this.pickPaymentType.bind(this);
    this.processPayment = this.processPayment.bind(this);
    this.state = {
      token: localStorage.getItem('token') || null,
      hidden: false,
      sum: 300,
      contractID: 194123,
      balans: 200, 
      date: '31.12.2020'
    };
  }

  toggleCardInfo() {
    const currentState = this.state.hidden;
    this.setState({ hidden: !currentState });
  }

  pickPaymentType() {

  }

  processPayment() {
    alert('Платёж проверяется, информация обновится автоматически')
  }

  render() {
    return (
      <div className="content">
        <div className="logo-wrapper">
          <img src="logo.png" className="logo" alt="Лого"></img>
          <h1>Мой интернет</h1>
        </div>
        
        <div className="info info_upper">
          <p>Номер договора: { this.state.contractID }</p>
          <p>Баланс: { this.state.balans } р.</p>
          <p>Дата оплаты: { this.state.date }</p>
          <p>Сумма к оплате: {this.state.sum } р.</p>
        </div>

        <div className="card_info {this.state.hidden ? 'hidden': null}">
          <p className="info">
            Переведите { this.state.sum } рублей на номер (Тут номер телефона, который привязан к карте нашего проекта)
            В комментарии <b>ОБЯЗАТЕЛЬНО</b> укажите номер своего договора: <b>{ this.state.contractID }</b>
          </p>
          <p>
            <button className="btn btn-pay" onClick={this.processPayment}>
              Я оплатил 
            </button>
          </p>
        </div>
      </div>
    )
  }
}

export default class App extends Component{
  render(){
    return(
      <Router>
        <div>
          <Route exact path="" component={ Home } />
          <Route exact path="/login" component={ Login } />
        </div>
      </Router>
    )
  }
}