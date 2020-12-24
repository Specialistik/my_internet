import React,{Component} from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import './App.css';

class Home extends Component {
  constructor(props) {
    super(props);
    this.toggleCardInfo = this.toggleCardInfo.bind(this);
    this.pickPaymentType = this.pickPaymentType.bind(this);
    this.processPayment = this.processPayment.bind(this);
    this.state = {
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

  processPayment(sum) {

  }

  updateSum(sum) {
    this.setState({ sum : sum})
  }

  render() {
    return (
      <div className="content">
        <div className="logo-wrapper">
          <img src="/img/logo.svg" className="logo" alt="Лого"></img>
        </div>

        <p><span class="label label-warning">Номер договора: { this.state.contractID } </span></p>
        <p><span class="label label-warning">Баланс: { this.state.balans } р.</span></p>
        <p><span class="label label-warning">Дата оплаты: { this.state.date }</span></p>
        <p><span class="label label-warning">Сумма к оплате: {this.state.sum } р.</span></p>

        <div className="card_info {this.state.hidden ? 'hidden': null}">
          <p className="info">
            Переведите { this.state.sum } рублей на номер (Тут номер телефона, который привязан к карте нашего проекта)
            В комментарии <b>ОБЯЗАТЕЛЬНО</b> укажите номер своего договора: <b>{ this.state.contractID }</b>
          </p>
          <p>
            <button className="btn btn-danger btn-pay" onClick={this.toggleCardInfo}>
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
          <Route exact path="/" component={Home} />
        </div>
    </Router>
      )
  }
}