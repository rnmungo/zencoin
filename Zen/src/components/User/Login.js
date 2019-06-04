import React, { Component } from 'react';
import logo from '../Global/img/money.png';
import '../Global/css/Login.css';
import '../Global/css/bootstrap.min.css';

class Login extends Component {
  render () {
    return (
      <div className="col-10 col-md-6 col-lg-4 shadow-lg border bg-white">
          <img src={logo} className="img-fluid img-circle my-2" style={{height: '4, rem'}} alt="logo" />
          <div className="form-group row">
              <div className="col-12">
                <label className="field a-field a-field_a2 page__field">
                  <input type="text" className="field__input a-field__input" placeholder=" " value="" required />
                  <span className="a-field__label-wrap">
                    <span className="a-field__label">Usuario</span>
                  </span>
                </label>
              </div>
          </div>
          <div className="form-group row">
              <div className="col-12">
                  <label className="field a-field a-field_a2 page__field">
                    <input type="password" className="field__input a-field__input" placeholder=" " value="" required />
                    <span className="a-field__label-wrap">
                      <span className="a-field__label">Contraseña</span>
                    </span>
                  </label>
              </div>
          </div>
          <div className="form-group row justify-content-center">
              <div className="col-12">
                  <button className="btn btn-primary rounded shadow">
                      Iniciar Sesión
                  </button>
              </div>
          </div>
      </div>
    );
  }
}

export default Login;
