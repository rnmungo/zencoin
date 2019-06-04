import React, { Component } from 'react';
import logo from '../Global/img/money.png';
import '../Global/css/Welcome.css';
import {Link} from 'react-router-dom';

class Welcome extends Component {
  render () {
    return (
      <div className="Welcome">
          <img src={logo} className="Logo" alt="logo" />
          <h2>Bienvenido a ZenCoin</h2>
          <Link to={'/login'} className="Link">Iniciar Sesión</Link>
      </div>
    );
  }
}

export default Welcome;
