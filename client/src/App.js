import React,{Component} from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import './App.css';

/*
const Home = ()=> <div className="content">
                    <div className="person_info">
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
*/

class Home extends Component {
  constructor(props) {
    super(props);
    this.toggleCardInfo = this.toggleCardInfo.bind(this);
    this.state = {
      hidden: false,
    };
  }

  toggleCardInfo() {
    const currentState = this.state.hidden;
    this.setState({ hidden: !currentState });
  }

  render() {
    return (
      <div className="content">
        <div className="person_info">
          <p><span class = "label label-warning">Баланс: 200 р.</span></p>
          <p><span class = "label label-warning">Дата оплаты: 31.12.2020</span></p>
          <p><span class = "label label-warning">Сумма к оплате: 300 р.</span></p>
          <button className="btn btn-danger btn-pay" onClick={this.toggleCardInfo}>
            Пополнить
          </button>
        </div>
        <div className="card_info {this.state.hidden ? 'hidden': null}">
          <div className="input-group mb-3 row">
            <input type="text" className="form-control col-md-12" placeholder="Номер карты"/>
          </div>
          <div className="input-group mb-3 row">
            <input type="text" className="form-control col-md-5" placeholder="Срок действия"/>
            <div className="col-md-1"></div>
            <input type="text" className="form-control col-md-5" placeholder="CVV/CVC"/>
          </div>
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