import React, { Component } from 'react';
import logo from '../Global/img/money.png';
import '../Global/css/Login.css';
import '../Global/css/bootstrap.min.css';
import axios from  'axios';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: '',
      error: ''
    }
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleLoginButton = this.handleLoginButton.bind(this);
  }

  handleInputChange(e) {
    if (e.target.id === 'email') {
      this.setState({
        email: e.target.value
      });
    }
    else if (e.target.id === 'password') {
      this.setState({
        password: e.target.value
      });
    }
  }

  handleLoginButton() {
    const { email, password } = this.state;
    const instance = axios.create({baseURL: 'http://localhost:9000'});
    instance.post('/auth', {
      email: email,
      password: password
    }).then((res) => {
      this.props.authenticate(res.token)
    }).catch((err) => {
      this.setState({
        error: 'El e-mail y contraseña no coinciden',
      });
    });
  }

  render () {
    return (
      <div className="Login">
          <img src={logo} className="Logo"  alt="logo" />
          <label className="field a-field a-field_a2 page__field">
            <input type="text" id="email"
                    className="field__input a-field__input"
                    placeholder=" " value={this.state.email}
                    onChange={this.handleInputChange}
                    autoComplete="off" required />
            <span className="a-field__label-wrap">
              <span className="a-field__label">E-Mail</span>
            </span>
          </label>
          <label className="field a-field a-field_a2 page__field">
            <input type="password" id="password"
                    className="field__input a-field__input"
                    placeholder=" " value={this.state.password}
                    onChange={this.handleInputChange} required />
            <span className="a-field__label-wrap">
              <span className="a-field__label">Contraseña</span>
            </span>
          </label>
          <button className="Button" onClick={this.handleLoginButton}>
              Iniciar Sesión
          </button>
          <p>{this.state.error}</p>
      </div>
    );
  }
}

export default Login;
