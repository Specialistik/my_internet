import React, { Component } from "react";
import { Button, HelpBlock, FormGroup, FormControl, ControlLabel } from "react-bootstrap";

function FieldGroup({ id, label, help, ...props }) {
  return (
    <FormGroup controlId={id}>
      <ControlLabel>{label}</ControlLabel>
      <FormControl {...props} />
      {help && <HelpBlock>{help}</HelpBlock>}
    </FormGroup>
  );
}

export default class Login extends Component{
  constructor(props){
    super(props);

    this.state = {
      username: "",
      password: "",
      state: localStorage.getItem('access_token')
    }

 }

  handleChange=event=>{
    const target = event.target;
    const value = target.value;
    const name = target.name;
    this.setState({
      [name]: value
    });
  }
/*
  handleRegistration = e =>{
    e.preventDefault() ;
    let url = "http://localhost:5000/register"
    let formData  = new FormData();
    let data = this.state;
    for(let name in data) {
      formData.append(name, data[name]);
    }

    fetch(url, {
      method: 'POST',
      body: formData
    }).then( res => res.json())
    .then(data=>{
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('username', data.username);
      if (localStorage.getItem("access_token") !== null && localStorage.getItem("access_token")!=="undefined") {
        window.location.replace("/")
      }else{
          alert(data.error)
      }
    }).catch(err => console.log(err));
  }
*/
  handleSignIn = e =>{
    console.log('before ajax request');
    e.preventDefault() ;
    let url = "http://localhost:5000/api/login"
    let formData  = new FormData();
    let data = this.state;
    for(let name in data) {
      formData.append(name, data[name]);
    }

    fetch(url, {
      method: 'POST',
      body: formData
    }).then( res => res.json())
    .then(data=>{
      console.log('after ajax ', data)
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('username', data.username);
      if (localStorage.getItem("access_token") !== null && localStorage.getItem("access_token")!=="undefined") {
        window.location.replace("/")
      }else{
          alert(data.error);
      }
    }).catch(err => console.log(err));
  }
  render(){
    return (
      <div className="LoginForm">
        <form>
          <FieldGroup
            id="formControlsEmail"
            type="email"
            name="username"
            label="Логин"
            value={this.state.username}
            onChange={this.handleChange}
            placeholder="Введите логин"
          />

          <FieldGroup 
            id="formControlsPassword" 
            type="password"
            name="password"
            label="Пароль" 
            value={this.state.password}
            onChange={this.handleChange}
            placeholder="Введите пароль"
          />

          <Button className="custom-btn" onClick={this.handleSignIn}>Войти</Button>
          </form>
      </div>
    );
  }
}